"""Arrays have length 1..10^5 and values in [-10^5,10^5]; includes 470 increasing/decreasing/constant patterns, random arrays, and three 100,000-element boundary patterns."""

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
    "candidate(nums=[1, 2, 2, 3])",
    "candidate(nums=[6, 5, 4, 4])",
    "candidate(nums=[1, 3, 2])",
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

    for case_id in range(470):
        length = rng.randint(1, 100)
        start = rng.randint(-10_000, 10_000)
        step = rng.randint(1, 100)
        mode = case_id % 3
        if mode == 0:
            nums = [start + index * step for index in range(length)]
        elif mode == 1:
            nums = [start - index * step for index in range(length)]
        else:
            nums = [start] * length
        calls.append({"nums": nums})

    for _ in range(180):
        calls.append(
            {
                "nums": [
                    rng.randint(-100_000, 100_000) for _ in range(rng.randint(1, 100))
                ]
            }
        )

    calls.extend(
        [
            {"nums": list(range(-50_000, 50_000))},
            {"nums": list(range(49_999, -50_001, -1))},
            {"nums": [0] * 100_000},
        ]
    )
    return _with_examples(_calls(calls))
