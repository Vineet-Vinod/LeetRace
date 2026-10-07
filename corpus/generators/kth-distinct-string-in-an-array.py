"""Array length is 1..60, strings use lowercase letters and length at most 2; k is sampled from [1,len(arr)]."""

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
    "candidate(arr=['d', 'b', 'c', 'b', 'c', 'a'], k=2)",
    "candidate(arr=['aaa', 'aa', 'a'], k=1)",
    "candidate(arr=['a', 'b', 'a'], k=3)",
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
        arr = [
            rng.choice(["a", "b", "c", "aa", "ab", "bc"])
            for _ in range(rng.randint(1, 60))
        ]
        calls.append({"arr": arr, "k": rng.randint(1, len(arr))})
    calls.append({"arr": ["abcde"] * 1000, "k": 1000})
    return _with_examples(_calls(calls))
