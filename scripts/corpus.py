"""Rebuild and verify bundled test suites from saved solutions and generators."""

import argparse
import ast
import base64
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from pathlib import Path
import re
import subprocess
import sys
from typing import Literal, cast
import zlib

from pydantic import BaseModel, ConfigDict, Field, JsonValue

from scripts.corpus_dataclasses import BuildResult
from server.sandbox import RUNNER_SCRIPT, _run_sync

ROOT = Path(__file__).resolve().parents[1]


class Problem(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: str
    title: str
    difficulty: Literal["Easy", "Medium", "Hard"]
    tags: list[str] = Field(default_factory=list)
    description: str
    starter_code: str
    entry_point: str
    preamble: str = ""
    test_cases: list[str] = Field(default_factory=list)
    check_function: str = ""
    time_limit_seconds: int = Field(default=5, ge=1, le=30)
    memory_limit_mb: int = Field(default=256, ge=64, le=1024)


class GeneratedCalls(BaseModel):
    calls: list[str]
    domain_size: int | None


class GoldenResult(BaseModel):
    tests: list[str]


class RepairRecord(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: str
    status: Literal["repaired", "deleted"]
    test_count: int = 0


class CompactLiterals(ast.NodeTransformer):
    def visit(self, node: ast.AST) -> ast.AST:
        if isinstance(node, ast.List) or (
            isinstance(node, ast.Constant) and isinstance(node.value, str)
        ):
            literal = ast.unparse(node)
            if len(literal) > 4096:
                if any(
                    isinstance(part, (ast.Tuple, ast.Set, ast.Dict))
                    for part in ast.walk(node)
                ):
                    return super().visit(node)
                try:
                    value = ast.literal_eval(node)
                except (ValueError, SyntaxError):
                    return super().visit(node)
                payload = base64.b64encode(
                    zlib.compress(json.dumps(value, ensure_ascii=False).encode())
                ).decode()
                if len(payload) < len(literal):
                    return ast.copy_location(
                        ast.Call(
                            func=ast.Name(id="test_data", ctx=ast.Load()),
                            args=[ast.Constant(value=payload)],
                            keywords=[],
                        ),
                        node,
                    )
        return super().visit(node)


def compact_test(test: str) -> str:
    tree = CompactLiterals().visit(ast.parse(test))
    return ast.unparse(ast.fix_missing_locations(tree))


def float_tolerances(description: str) -> tuple[float, float]:
    for match in re.finditer(r"(?:10\s*\^?\s*-\s*|1e-)([1-9])\b", description):
        context = description[max(0, match.start() - 100) : match.end() + 100].lower()
        if not any(word in context for word in ("accepted", "error", "differ")):
            continue
        tolerance = 10.0 ** -int(match.group(1))
        return tolerance, tolerance if "relative" in context else 0.0
    return 1e-6, 0.0


# The same node definitions and comparison helpers as submissions use.
GOLDEN_SCRIPT = (
    RUNNER_SCRIPT.split("data = json.loads(sys.stdin.read())", 1)[0]
    + """
import contextlib, io, math
data = json.loads(sys.stdin.read())
ns = dict(globals())
with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
    exec(data['preamble'], ns)
    ns['pow'] = pow
    exec(data['code'], ns)
    tests = []
    def has_float(value):
        if isinstance(value, float):
            return True
        if isinstance(value, (list, tuple)):
            return any(has_float(item) for item in value)
        return False
    def as_floats(value):
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return float(value)
        if isinstance(value, list):
            return [as_floats(item) for item in value]
        if isinstance(value, tuple):
            return tuple(as_floats(item) for item in value)
        return value
    for call in data['calls']:
        ns['candidate'] = eval(data['entry_point'], ns)
        answer = eval(call, ns)
        if data.get('float_output', False):
            answer = as_floats(answer)
        if isinstance(answer, TreeNode):
            test = f'assert is_same_tree({call}, {answer!r})'
        elif isinstance(answer, ListNode):
            test = f'assert is_same_list({call}, {answer!r})'
        else:
            literal = repr(answer)
            if isinstance(answer, (list, tuple)) and len(literal) > 64000:
                encoded = base64.b64encode(zlib.compress(json.dumps(answer).encode())).decode()
                literal = f'expected_output({encoded!r})'
            if has_float(answer):
                if not is_close(answer, answer, 0, 0):
                    raise ValueError('Expected finite floats')
                test = f'assert is_close({call}, {literal}, {data["absolute_tolerance"]!r}, {data["relative_tolerance"]!r})'
            else:
                test = f'assert {call} == {literal}'
        compile(test, '<generated-test>', 'exec')
        tests.append(test)
print(json.dumps({'tests': tests}))
"""
)

GENERATOR_SCRIPT = """
import contextlib, importlib.util, io, json, sys
path, seed = sys.argv[1], int(sys.argv[2])
spec = importlib.util.spec_from_file_location('generator', path)
module = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
    spec.loader.exec_module(module)
    calls = module.generate(seed)
print(json.dumps({'calls': calls, 'domain_size': getattr(module, 'DOMAIN_SIZE', None)}))
"""


def load_calls(problem_id: str, seed: int) -> tuple[list[str], int | None]:
    path = ROOT / "corpus" / "generators" / f"{problem_id}.py"
    proc = subprocess.run(
        [sys.executable, "-c", GENERATOR_SCRIPT, str(path), str(seed)],
        capture_output=True,
        text=True,
        timeout=30,
    )
    if proc.returncode:
        raise ValueError(f"{problem_id}: generator failed: {proc.stderr[-3000:]}")
    generated = GeneratedCalls.model_validate_json(proc.stdout)
    calls = generated.calls
    keys = [
        ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        for call in calls
    ]
    if len(keys) != len(set(keys)):
        raise ValueError("Generator returned duplicate inputs")
    domain_size = generated.domain_size
    if not 500 <= len(calls) <= 999:
        if not calls or len(calls) >= 500 or domain_size != len(calls):
            raise ValueError(
                "Need 500-999 cases, or enumerate a smaller complete DOMAIN_SIZE"
            )
    return sorted(calls), domain_size


def verify(problem_id: str, problem: Problem, code: str) -> BuildResult:
    result = _run_sync(
        code,
        problem.entry_point,
        problem.test_cases,
        problem.preamble,
        time_limit_seconds=problem.time_limit_seconds,
        memory_limit_mb=problem.memory_limit_mb,
    )
    if result["passed"] != len(problem.test_cases) or result.get("error"):
        raise ValueError(f"{problem_id}: sandbox verification failed: {result}")
    return BuildResult(problem_id, len(problem.test_cases), result["time_ms"])


def build(problem_id: str, seed: int = 0) -> BuildResult:
    path = ROOT / "problems" / f"{problem_id}.json"
    original = path.read_text()
    problem = Problem.model_validate_json(original)
    code = (ROOT / "corpus" / "solutions" / f"{problem_id}.py").read_text()
    calls, domain_size = load_calls(problem_id, seed)
    absolute_tolerance, relative_tolerance = float_tolerances(problem.description)
    proc = subprocess.run(
        [sys.executable, "-c", GOLDEN_SCRIPT],
        input=json.dumps(
            {
                "code": code,
                "preamble": problem.preamble,
                "entry_point": problem.entry_point,
                "calls": calls,
                "absolute_tolerance": absolute_tolerance,
                "relative_tolerance": relative_tolerance,
                "float_output": bool(
                    re.search(
                        r"->\s*(?:float|(?:List|list)\[float\])\s*:",
                        problem.starter_code,
                    )
                ),
            }
        ),
        capture_output=True,
        text=True,
        timeout=30,
    )
    if proc.returncode:
        raise ValueError(f"{problem_id}: golden solution failed: {proc.stderr[-3000:]}")
    problem.test_cases = [
        compact_test(test)
        for test in GoldenResult.model_validate_json(proc.stdout).tests
    ]
    problem.check_function = "def check(candidate):\n" + "\n".join(
        f"    {test}" for test in problem.test_cases
    )
    result = verify(problem_id, problem, code)
    dumped = cast(dict[str, JsonValue], problem.model_dump())
    field_order = (
        "id",
        "title",
        "difficulty",
        "tags",
        "description",
        "entry_point",
        "starter_code",
        "preamble",
        "check_function",
        "test_cases",
    )
    data = {key: dumped.pop(key) for key in field_order if key in dumped}
    data.update(dumped)
    data["output_order"] = "strict"
    data["generator_seed"] = seed
    if domain_size is not None:
        data["test_domain_size"] = domain_size
    else:
        data.pop("test_domain_size", None)
    if path.read_text() != original:
        raise ValueError(f"{problem_id}: problem changed during rebuild; retry")
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    return result


def verify_saved(problem_id: str) -> BuildResult:
    problem = Problem.model_validate_json(
        (ROOT / "problems" / f"{problem_id}.json").read_text()
    )
    code = (ROOT / "corpus" / "solutions" / f"{problem_id}.py").read_text()
    return verify(problem_id, problem, code)


def finalize_index() -> None:
    records: dict[str, RepairRecord] = {}
    reports = sorted(
        (ROOT / "corpus" / "reports").glob("*.json"), key=lambda p: p.stat().st_mtime
    )
    for path in reports:
        raw = cast(JsonValue, json.loads(path.read_text()))
        rows = raw.get("problems") if isinstance(raw, dict) else raw
        if not isinstance(rows, list):
            raise ValueError(f"{path}: expected a report list or a problems list")
        for row in rows:
            if not isinstance(row, dict) or row.get("status") not in (
                "repaired",
                "deleted",
            ):
                continue
            record = RepairRecord.model_validate(row)
            previous = records.get(record.id)
            if previous and previous.status != record.status:
                raise ValueError(f"Conflicting report status for {record.id}")
            records[record.id] = record

    index_path = ROOT / "problems" / "index.json"
    entries = cast(list[dict[str, JsonValue]], json.loads(index_path.read_text()))
    kept: list[dict[str, JsonValue]] = []
    for entry in entries:
        problem_id = cast(str, entry["id"])
        if problem_id not in records:
            raise ValueError(f"Missing completed repair report for {problem_id}")
        record = records[problem_id]
        path = ROOT / "problems" / f"{problem_id}.json"
        if record.status == "deleted":
            if path.exists():
                raise ValueError(f"Deleted problem still exists: {problem_id}")
            continue
        problem = Problem.model_validate_json(path.read_text())
        if problem.id != problem_id:
            raise ValueError(f"Problem ID mismatch: {problem_id}")
        if len(problem.test_cases) != record.test_count:
            raise ValueError(f"Report/test count mismatch: {problem_id}")
        if problem.check_function != "def check(candidate):\n" + "\n".join(
            f"    {test}" for test in problem.test_cases
        ):
            raise ValueError(f"check_function differs from test_cases: {problem_id}")
        expected_count = len(problem.test_cases)
        extra = problem.model_extra or {}
        if extra.get("output_order") != "strict":
            raise ValueError(f"Not repaired with strict output order: {problem_id}")
        if (
            not 500 <= expected_count <= 999
            and extra.get("test_domain_size") != expected_count
        ):
            raise ValueError(f"Invalid testcase count: {problem_id}")
        for directory in ("solutions", "generators"):
            if not (ROOT / "corpus" / directory / f"{problem_id}.py").exists():
                raise ValueError(f"Missing {directory} artifact: {problem_id}")
        entry.update(
            {
                "title": problem.title,
                "difficulty": problem.difficulty,
                "tags": [cast(JsonValue, tag) for tag in problem.tags],
                "test_count": expected_count,
                "verified": True,
            }
        )
        kept.append(entry)
    index_path.write_text(json.dumps(kept, ensure_ascii=False, indent=2) + "\n")
    print(f"Indexed {len(kept)} repaired problems; removed {len(entries) - len(kept)}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["build", "verify", "index"])
    parser.add_argument("ids", nargs="*")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()
    if args.action == "index":
        finalize_index()
        return
    ids = args.ids or [
        entry["id"]
        for entry in json.loads((ROOT / "problems" / "index.json").read_text())
    ]
    if args.action == "build":
        for problem_id in ids:
            result = build(problem_id, args.seed)
            print(
                f"{result.problem_id}: {result.test_count} tests passed in {result.time_ms} ms"
            )
        return
    failed: dict[str, str] = {}
    test_count = 0
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(verify_saved, problem_id): problem_id for problem_id in ids
        }
        for i, future in enumerate(as_completed(futures), 1):
            problem_id = futures[future]
            try:
                result = future.result()
                test_count += result.test_count
                if args.ids or i % 100 == 0 or i == len(ids):
                    print(
                        f"{i}/{len(ids)} verified; {problem_id}: {result.test_count} tests in {result.time_ms} ms",
                        flush=True,
                    )
            except Exception as error:
                failed[problem_id] = str(error)
                print(f"FAIL {problem_id}: {error}", flush=True)
    print(f"Verified {len(ids) - len(failed)}/{len(ids)} problems, {test_count} tests")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
