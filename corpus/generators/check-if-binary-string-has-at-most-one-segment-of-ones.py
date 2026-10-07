"""Strings have length 1..100, contain only binary digits, begin with 1, and include 300 single-segment patterns plus random multi-segment patterns."""

import ast
import random


def _calls(cases: list[dict[str, object]]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for case in cases:
        args = ", ".join(f"{key}={value!r}" for key, value in case.items())
        call = f"candidate({args})"
        if call not in seen:
            seen.add(call)
            out.append(call)
    assert len(out) >= 500, len(out)
    assert len(out) <= 999, len(out)
    return out


EXAMPLE_CALLS = ["candidate(s='1001')", "candidate(s='110')"]


def _with_examples(generated: list[str]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for call in EXAMPLE_CALLS + generated:
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        if key not in seen:
            seen.add(key)
            result.append(call)
    assert 500 <= len(result) <= 999, len(result)
    return result


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = [{"s": "1"}, {"s": "10"}, {"s": "1001"}, {"s": "111"}]
    for _ in range(620):
        n = rng.randint(1, 100)
        s = "1" + "".join(rng.choice("01") for _ in range(n - 1))
        calls.append({"s": s})
    for case_id in range(300):
        ones = 1 + case_id % 30
        zeros = case_id // 30
        calls.append({"s": "1" * ones + "0" * zeros})
    calls.append({"s": "1" + "0" * 99})
    return _with_examples(_calls(calls))
