"""Calories are in [0,200], 1 <= k <= n <= 50, and lower/upper are ordered nonnegative bounds."""

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
    "candidate(calories=[1, 2, 3, 4, 5], k=1, lower=3, upper=3)",
    "candidate(calories=[3, 2], k=2, lower=0, upper=1)",
    "candidate(calories=[6, 5, 0, 0], k=2, lower=1, upper=5)",
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
        n = rng.randint(1, 50)
        cal = [rng.randint(0, 200) for _ in range(n)]
        k = rng.randint(1, n)
        lo = rng.randint(0, 500)
        hi = rng.randint(lo, 600)
        calls.append({"calories": cal, "k": k, "lower": lo, "upper": hi})
    calls.append({"calories": [20_000] * 100_000, "k": 100_000, "lower": 0, "upper": 0})
    return _with_examples(_calls(calls))
