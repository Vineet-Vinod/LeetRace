"""Arrays have length 2..100, values in [1,1000], and k in [1,2000]."""

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
    "candidate(nums=[34, 23, 1, 24, 75, 33, 54, 8], k=60)",
    "candidate(nums=[10, 20, 30], k=15)",
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
                "nums": [rng.randint(1, 1000) for _ in range(rng.randint(2, 100))],
                "k": rng.randint(1, 2000),
            }
        )
    calls.append({"nums": [1000] * 100, "k": 2000})
    return _with_examples(_calls(calls))
