"""Arrays have length 1..1000 and values in [-1000,1000]; five length-1000 cases supplement modest random arrays."""

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
    "candidate(nums=[1, 2, 3, 4])",
    "candidate(nums=[1, 1, 1, 1, 1])",
    "candidate(nums=[3, 1, 2, 10, 1])",
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
    for _ in range(645):
        calls.append(
            {"nums": [rng.randint(-1000, 1000) for _ in range(rng.randint(1, 80))]}
        )
    for _ in range(5):
        calls.append({"nums": [rng.randint(-1000, 1000) for _ in range(1000)]})
    calls.append({"nums": [1_000_000] * 1000})
    return _with_examples(_calls(calls))
