"""Array is nonempty with values and target in [1,10^4]; target is explicitly inserted and start is valid."""

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
    "candidate(nums=[1, 2, 3, 4, 5], target=5, start=3)",
    "candidate(nums=[1], target=1, start=0)",
    "candidate(nums=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], target=1, start=0)",
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
        n = rng.randint(1, 100)
        target = rng.randint(1, 10)
        nums = [rng.randint(1, 10) for _ in range(n)]
        nums[rng.randrange(n)] = target
        calls.append({"nums": nums, "target": target, "start": rng.randrange(n)})
    calls.append({"nums": [10_000] + [1] * 999, "target": 10_000, "start": 999})
    return _with_examples(_calls(calls))
