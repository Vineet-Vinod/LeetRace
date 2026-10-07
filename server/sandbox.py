"""Execute user code in a sandboxed subprocess with resource limits.

Security model:
  - Each submission runs in a separate subprocess via subprocess.run().
  - Resource limits (CPU time, memory, file size, process count) are set
    via the POSIX resource module (Linux and macOS). On platforms where
    resource limits are unavailable, the subprocess relies solely on the
    wall-clock timeout.
  - The subprocess has full filesystem read access. This sandbox does NOT
    provide filesystem isolation. For production use, consider running
    inside a container or seccomp-bpf sandbox.
  - Network access is not restricted at this layer.
"""

import asyncio
import json
import logging
import subprocess
import sys
import textwrap
import time

logger = logging.getLogger(__name__)

_SUBPROCESS_TIMEOUT_SECONDS = 10

# Limit concurrent sandbox subprocess executions to avoid CPU saturation when
# many players submit simultaneously. Each subprocess is CPU-bound, so running
# more than ~4 at once on a typical host provides no throughput benefit and
# degrades latency for every in-flight submission.
_MAX_CONCURRENT_SUBMISSIONS = 4
_submission_semaphore = asyncio.Semaphore(_MAX_CONCURRENT_SUBMISSIONS)

# Resource limits applied to the sandbox subprocess (POSIX only).
_CPU_LIMIT_SECONDS = 5
_MEMORY_LIMIT_BYTES = 256 * 1024 * 1024  # 256 MB
_FILE_SIZE_LIMIT_BYTES = 1024 * 1024  # 1 MB
_MAX_CHILD_PROCESSES = 0  # no forking


RUNNER_SCRIPT = textwrap.dedent("""\
    import ast, base64, json, math, sys, time, re, zlib
    from collections import deque

    # --- TreeNode helpers ---
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
        def __repr__(self):
            vals = []
            q = deque([self])
            while q:
                node = q.popleft()
                if node:
                    vals.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    vals.append(None)
            while vals and vals[-1] is None:
                vals.pop()
            return f"tree_node({vals})"

    def tree_node(vals):
        if not vals:
            return None
        root = TreeNode(vals[0])
        q = deque([root])
        i = 1
        while q and i < len(vals):
            node = q.popleft()
            if i < len(vals) and vals[i] is not None:
                node.left = TreeNode(vals[i])
                q.append(node.left)
            i += 1
            if i < len(vals) and vals[i] is not None:
                node.right = TreeNode(vals[i])
                q.append(node.right)
            i += 1
        return root

    def is_same_tree(a, b):
        pending = [(a, b)]
        while pending:
            left, right = pending.pop()
            if left is None or right is None:
                if left is not right:
                    return False
                continue
            if left.val != right.val:
                return False
            pending.extend(((left.left, right.left), (left.right, right.right)))
        return True

    # --- ListNode helpers ---
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
        def __repr__(self):
            vals, node = [], self
            while node:
                vals.append(node.val)
                node = node.next
            return f"list_node({vals})"

    def list_node(vals):
        head = ListNode(0)
        cur = head
        for v in vals:
            cur.next = ListNode(v)
            cur = cur.next
        return head.next

    def is_same_list(a, b):
        while a and b:
            if a.val != b.val:
                return False
            a, b = a.next, b.next
        return a is None and b is None

    def prepare_test(raw, any_order):
        tree = ast.parse(raw)
        statement = tree.body[0]
        test = statement.test if isinstance(statement, ast.Assert) else None
        equality = isinstance(test, ast.Compare) and len(test.ops) == 1 and isinstance(test.ops[0], ast.Eq)
        call = test.left if equality else tree
        for node in ast.walk(call):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'candidate':
                if all(keyword.arg is not None for keyword in node.keywords):
                    node.args.extend(keyword.value for keyword in node.keywords)
                    node.keywords = []
        if equality:
            comparison = 'flex_eq' if any_order else 'normalize_eq'
            tree.body[0:1] = [
                ast.Assign(targets=[ast.Name(id='_actual_', ctx=ast.Store())], value=test.left),
                ast.Assign(targets=[ast.Name(id='_expected_', ctx=ast.Store())], value=test.comparators[0]),
                ast.parse(f"assert {comparison}(_actual_, _expected_), 'Expected ' + repr(_expected_) + ' but got ' + repr(_actual_)").body[0],
            ]
        return compile(ast.fix_missing_locations(tree), '<testcase>', 'exec')

    def _normalize(x):
        if isinstance(x, (list, tuple)):
            return [_normalize(i) for i in x]
        return x

    def _sort_key(x):
        if isinstance(x, list):
            return (1, str(_deep_sort(x)))
        try:
            return (0, x)
        except TypeError:
            return (0, str(x))

    def _deep_sort(x):
        if isinstance(x, list):
            return sorted([_deep_sort(i) for i in x], key=_sort_key)
        return x

    def flex_eq(a, b):
        a, b = _normalize(a), _normalize(b)
        if a == b:
            return True
        if isinstance(a, list) and isinstance(b, list):
            return _deep_sort(a) == _deep_sort(b)
        return False

    def normalize_eq(a, b):
        return _normalize(a) == _normalize(b)

    def expected_output(payload):
        return json.loads(zlib.decompress(base64.b64decode(payload)))

    test_data = expected_output

    def is_close(actual, expected, absolute_tolerance, relative_tolerance=0.0):
        if isinstance(expected, float):
            if isinstance(actual, bool) or not isinstance(actual, (int, float)):
                return False
            return math.isfinite(actual) and math.isfinite(expected) and math.isclose(
                actual, expected, abs_tol=absolute_tolerance, rel_tol=relative_tolerance)
        if isinstance(expected, (list, tuple)):
            return isinstance(actual, (list, tuple)) and len(actual) == len(expected) and all(
                is_close(a, b, absolute_tolerance, relative_tolerance) for a, b in zip(actual, expected))
        return actual == expected

    data = json.loads(sys.stdin.read())
    code = data["code"]
    entry_point = data["entry_point"]
    any_order = data.get("any_order", False)
    test_cases = data["test_cases"]
    preamble = data.get("preamble", "")

    import io

    # Redirect stdout/stderr to capture user output
    real_stdout = sys.stdout
    captured_out = io.StringIO()
    captured_err = io.StringIO()
    sys.stdout = captured_out
    sys.stderr = captured_err

    # Execute preamble (imports needed by starter code like List, Optional, etc.)
    namespace = {
        "TreeNode": TreeNode,
        "ListNode": ListNode,
    }
    if preamble:
        try:
            exec(preamble, namespace)
        except Exception:
            pass
    namespace["pow"] = pow

    # Execute user code
    try:
        exec(code, namespace)
    except SyntaxError as e:
        # Special handling for "expected an indented block" errors
        if "expected an indented block" in str(e).lower() and code.rstrip().endswith(':'):
            # User submitted incomplete code (function/class without body)
            # Try again with a pass statement appended
            try:
                fixed_code = code.rstrip() + '\\n        pass'
                exec(fixed_code, namespace)
            except Exception as retry_e:
                sys.stdout = real_stdout
                print(json.dumps({"passed": 0, "total": len(test_cases), "error": f"Compilation error: {retry_e}",
                                   "stdout": captured_out.getvalue()[:5000], "stderr": captured_err.getvalue()[:5000]}))
                sys.exit(0)
        else:
            sys.stdout = real_stdout
            print(json.dumps({"passed": 0, "total": len(test_cases), "error": f"Compilation error: {e}",
                               "stdout": captured_out.getvalue()[:5000], "stderr": captured_err.getvalue()[:5000]}))
            sys.exit(0)
    except Exception as e:
        sys.stdout = real_stdout
        print(json.dumps({"passed": 0, "total": len(test_cases), "error": f"Compilation error: {e}",
                           "stdout": captured_out.getvalue()[:5000], "stderr": captured_err.getvalue()[:5000]}))
        sys.exit(0)

    # Resolve entry_point — supports both bare names and expressions like Solution().twoSum
    try:
        candidate = eval(entry_point, namespace)
    except Exception as e:
        sys.stdout = real_stdout
        print(json.dumps({"passed": 0, "total": len(test_cases), "error": f"Cannot resolve '{entry_point}': {e}",
                           "stdout": captured_out.getvalue()[:5000], "stderr": captured_err.getvalue()[:5000]}))
        sys.exit(0)

    # Inject as 'candidate' into test namespace (test cases call candidate(...))
    test_ns = dict(namespace)
    test_ns["candidate"] = candidate
    test_ns["flex_eq"] = flex_eq
    test_ns["normalize_eq"] = normalize_eq
    test_ns["expected_output"] = expected_output
    test_ns["test_data"] = test_data
    test_ns["is_close"] = is_close
    test_ns["tree_node"] = tree_node
    test_ns["list_node"] = list_node
    test_ns["is_same_tree"] = is_same_tree
    test_ns["is_same_list"] = is_same_list

    passed = 0
    total = len(test_cases)
    first_error = None
    first_failure = None

    def _parse_raw_tc(raw):
        \"\"\"Extract the named args and expected value from a raw test case.\"\"\"
        statement = ast.parse(raw).body[0]
        if isinstance(statement, ast.Assert) and isinstance(statement.test, ast.Compare):
            test = statement.test
            if len(test.ops) == 1 and isinstance(test.ops[0], ast.Eq):
                call = ast.unparse(test.left)
                if call.startswith('candidate('):
                    call = call[len('candidate('):-1]
                return call, ast.unparse(test.comparators[0])
        return re.sub(r'^assert\\s+', '', raw).strip(), None

    for orig_tc in test_cases:
        test_ns.pop('_actual_', None)
        test_ns.pop('_expected_', None)
        try:
            test_ns['candidate'] = eval(entry_point, namespace)
            exec(prepare_test(orig_tc, any_order), test_ns)
            passed += 1
        except AssertionError as e:
            if first_error is None:
                first_error = str(e)[:200] if str(e) else f"Assertion failed: {orig_tc[:100]}"
            if first_failure is None:
                args_str, expected_expr = _parse_raw_tc(orig_tc)
                first_failure = {
                    "input": args_str[:500],
                    "expected": repr(test_ns.get("_expected_"))[:300] if "_expected_" in test_ns else expected_expr,
                    "actual": repr(test_ns.get("_actual_"))[:300] if "_actual_" in test_ns else None,
                }
        except Exception as e:
            if first_error is None:
                first_error = f"Runtime error: {type(e).__name__}: {e}"
            if first_failure is None:
                args_str, expected_expr = _parse_raw_tc(orig_tc)
                first_failure = {
                    "input": args_str[:500],
                    "expected": expected_expr,
                    "actual": f"{type(e).__name__}: {e}"[:300],
                }

    sys.stdout = real_stdout
    result = {"passed": passed, "total": total, "error": first_error,
              "first_failure": first_failure,
              "stdout": captured_out.getvalue()[:5000], "stderr": captured_err.getvalue()[:5000]}
    print(json.dumps(result))
""")


def _set_limits(
    cpu_seconds: int = _CPU_LIMIT_SECONDS, memory_bytes: int = _MEMORY_LIMIT_BYTES
):
    """Set POSIX resource limits for the child process (Linux and macOS)."""
    try:
        import resource

        resource.setrlimit(resource.RLIMIT_CPU, (cpu_seconds, cpu_seconds))
        resource.setrlimit(resource.RLIMIT_AS, (memory_bytes, memory_bytes))
        resource.setrlimit(
            resource.RLIMIT_FSIZE, (_FILE_SIZE_LIMIT_BYTES, _FILE_SIZE_LIMIT_BYTES)
        )
        resource.setrlimit(
            resource.RLIMIT_NPROC, (_MAX_CHILD_PROCESSES, _MAX_CHILD_PROCESSES)
        )
    except (ImportError, ValueError, OSError) as e:
        logger.warning(
            "Sandbox resource limits could not be applied (%s). Code will run without limits.",
            e,
        )


def _run_sync(
    code: str,
    entry_point: str,
    test_cases: list[str],
    preamble: str = "",
    any_order: bool = False,
    time_limit_seconds: int = _CPU_LIMIT_SECONDS,
    memory_limit_mb: int = _MEMORY_LIMIT_BYTES // (1024 * 1024),
) -> dict:
    """Synchronous sandbox execution."""
    payload = json.dumps(
        {
            "code": code,
            "entry_point": entry_point,
            "test_cases": test_cases,
            "preamble": preamble,
            "any_order": any_order,
        }
    )

    wall_timeout = max(_SUBPROCESS_TIMEOUT_SECONDS, time_limit_seconds + 5)
    start = time.monotonic()
    try:
        proc = subprocess.run(
            [sys.executable, "-c", RUNNER_SCRIPT],
            input=payload,
            capture_output=True,
            text=True,
            timeout=wall_timeout,
            preexec_fn=lambda: _set_limits(
                time_limit_seconds, memory_limit_mb * 1024 * 1024
            ),
        )
        elapsed_ms = int((time.monotonic() - start) * 1000)

        if proc.returncode != 0 and not proc.stdout.strip():
            stderr = proc.stderr.strip()[:200]
            return {
                "passed": 0,
                "total": len(test_cases),
                "error": stderr or "Process crashed",
                "first_failure": None,
                "time_ms": elapsed_ms,
            }

        result = json.loads(proc.stdout.strip())
        result["time_ms"] = elapsed_ms
        return result

    except subprocess.TimeoutExpired:
        elapsed_ms = int((time.monotonic() - start) * 1000)
        return {
            "passed": 0,
            "total": len(test_cases),
            "error": f"Time limit exceeded ({wall_timeout}s)",
            "first_failure": None,
            "time_ms": elapsed_ms,
        }
    except json.JSONDecodeError as e:
        elapsed_ms = int((time.monotonic() - start) * 1000)
        return {
            "passed": 0,
            "total": len(test_cases),
            "error": f"Runner produced invalid output: {e}",
            "first_failure": None,
            "time_ms": elapsed_ms,
        }
    except Exception as e:
        elapsed_ms = int((time.monotonic() - start) * 1000)
        return {
            "passed": 0,
            "total": len(test_cases),
            "error": str(e)[:200],
            "first_failure": None,
            "time_ms": elapsed_ms,
        }


async def run_code(
    code: str,
    entry_point: str,
    test_cases: list[str],
    preamble: str = "",
    any_order: bool = False,
    time_limit_seconds: int = _CPU_LIMIT_SECONDS,
    memory_limit_mb: int = _MEMORY_LIMIT_BYTES // (1024 * 1024),
) -> dict:
    """Run user code in a sandbox. Returns {passed, total, error, time_ms}."""
    # Acquire the semaphore before spawning the subprocess so that at most
    # _MAX_CONCURRENT_SUBMISSIONS subprocesses run simultaneously. The I/O
    # wait before the semaphore is intentionally excluded — only the actual
    # CPU-bound subprocess execution is counted against the limit.
    async with _submission_semaphore:
        return await asyncio.to_thread(
            _run_sync,
            code,
            entry_point,
            test_cases,
            preamble,
            any_order,
            time_limit_seconds,
            memory_limit_mb,
        )
