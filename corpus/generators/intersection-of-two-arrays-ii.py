"""Both arrays are nonempty, length at most 50, and values in [0,20], within the stated [0,1000] bound."""

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
    "candidate(nums1=[1, 2, 2, 1], nums2=[2, 2])",
    "candidate(nums1=[4, 9, 5], nums2=[9, 4, 9, 8, 4])",
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
                "nums1": [rng.randint(0, 20) for _ in range(rng.randint(1, 50))],
                "nums2": [rng.randint(0, 20) for _ in range(rng.randint(1, 50))],
            }
        )
    calls.append({"nums1": [1000] * 1000, "nums2": [1000] * 1000})
    return _with_examples(_calls(calls))
