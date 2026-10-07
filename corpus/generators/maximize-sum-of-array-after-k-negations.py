"""Array values are in [-100,100], length is at most 50, and k is in [1,10^4]."""

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
    "candidate(nums=[4, 2, 3], k=1)",
    "candidate(nums=[3, -1, 0, 2], k=3)",
    "candidate(nums=[2, -3, -1, 5, -4], k=2)",
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
        calls.append(
            {
                "nums": [rng.randint(-100, 100) for _ in range(rng.randint(1, 50))],
                "k": rng.randint(1, 10_000),
            }
        )
    calls.append({"nums": [-100] * 5000 + [100] * 5000, "k": 10_000})
    return _with_examples(_calls(calls))
