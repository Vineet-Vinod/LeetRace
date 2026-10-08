"""Ticket counts are positive in [1,100], arrays have length 1..80, and k is valid."""

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
    "candidate(tickets=[2, 3, 2], k=2)",
    "candidate(tickets=[5, 1, 1, 1], k=0)",
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
        n = rng.randint(1, 80)
        calls.append(
            {"tickets": [rng.randint(1, 100) for _ in range(n)], "k": rng.randrange(n)}
        )
    calls.append({"tickets": [100] * 100, "k": 99})
    return _with_examples(_calls(calls))
