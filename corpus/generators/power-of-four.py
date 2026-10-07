"""All 16 positive powers 4^0 through 4^15 fit signed 32-bit; 4^16 exceeds the upper bound. Each valid power and both integer endpoints are generated."""

import ast
import random


def _calls(cases: list[dict[str, object]]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for case in cases:
        arguments = ", ".join(f"{key}={value!r}" for key, value in case.items())
        call = f"candidate({arguments})"
        if call not in seen:
            seen.add(call)
            result.append(call)
    assert 500 <= len(result) <= 999, len(result)
    return result


EXAMPLE_CALLS = ["candidate(n=16)", "candidate(n=5)", "candidate(n=1)"]


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
    calls: list[dict[str, object]] = []
    for _ in range(650):
        calls.append({"n": rng.randint(-(2**31), 2**31 - 1)})
    calls.extend([{"n": -(2**31)}, {"n": 2**31 - 1}, {"n": 4**15}])
    calls.extend({"n": 4**power} for power in range(16))
    result = _calls(calls)
    assert all(f"candidate(n={4**power})" in result for power in range(16))
    return _with_examples(result)
