"""Sorted nonempty arrays and targets are in [1,10^9]; includes length 1000, target 10^9, strict majorities, and exact-half negatives."""

import ast
import random


def _calls(cases: list[dict[str, object]]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for case in cases:
        args = ", ".join(f"{key}={value!r}" for key, value in case.items())
        call = f"candidate({args})"
        if call not in seen:
            seen.add(call)
            out.append(call)
    assert len(out) >= 500, len(out)
    assert len(out) <= 999, len(out)
    return out


EXAMPLE_CALLS = [
    "candidate(nums=[2, 4, 5, 5, 5, 5, 5, 6, 6], target=5)",
    "candidate(nums=[10, 100, 101, 101], target=101)",
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
    calls = []
    for _ in range(620):
        n = rng.randint(1, 60)
        values = sorted(rng.randint(1, 30) for _ in range(n))
        target = rng.randint(1, 30)
        calls.append({"nums": values, "target": target})
    calls.extend(
        [{"nums": [1, 2, 2, 2], "target": 2}, {"nums": [1, 2, 2, 3], "target": 2}]
    )
    for length in range(101, 241):
        majority = length // 2 + 1
        calls.append({"nums": [1] * majority + [2] * (length - majority), "target": 1})
        even_length = length if length % 2 == 0 else length + 1
        calls.append(
            {"nums": [1] * (even_length // 2) + [2] * (even_length // 2), "target": 1}
        )
    calls.extend(
        [
            {"nums": [1] * 500 + [2] * 500, "target": 1_000_000_000},
            {"nums": [1] * 501 + [2] * 499, "target": 1},
        ]
    )
    return _with_examples(_calls(calls))
