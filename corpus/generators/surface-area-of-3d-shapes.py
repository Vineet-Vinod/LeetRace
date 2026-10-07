"""Square grids have side length 1..12 and heights in [0,20]."""

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
    "candidate(grid=[[1, 2], [3, 4]])",
    "candidate(grid=[[1, 1, 1], [1, 0, 1], [1, 1, 1]])",
    "candidate(grid=[[2, 2, 2], [2, 1, 2], [2, 2, 2]])",
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
        n = rng.randint(1, 12)
        calls.append(
            {"grid": [[rng.randint(0, 20) for _ in range(n)] for _ in range(n)]}
        )
    calls.append({"grid": [[50] * 50 for _ in range(50)]})
    return _with_examples(_calls(calls))
