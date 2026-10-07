"""Even array length is 2..50 and values are in [1,50]."""

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


EXAMPLE_CALLS = [
    "candidate(nums=[7, 8, 3, 4, 15, 13, 4, 1])",
    "candidate(nums=[1, 9, 8, 3, 10, 5])",
    "candidate(nums=[1, 2, 3, 7, 8, 9])",
]


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
        n = rng.randint(1, 25) * 2
        calls.append({"nums": [rng.randint(1, 50) for _ in range(n)]})
    calls.append({"nums": [1] * 25 + [50] * 25})
    return _with_examples(_calls(calls))
