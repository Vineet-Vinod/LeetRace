"""Generated words and chars are lowercase; lengths and word counts remain within stated limits."""

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
    "candidate(words=['cat', 'bt', 'hat', 'tree'], chars='atach')",
    "candidate(words=['hello', 'world', 'leetcode'], chars='welldonehoneyr')",
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
        chars = "".join(rng.choice("abcde") for _ in range(rng.randint(1, 30)))
        words = [
            "".join(rng.choice("abcde") for _ in range(rng.randint(1, 10)))
            for _ in range(rng.randint(1, 20))
        ]
        calls.append({"words": words, "chars": chars})
    calls.append({"words": ["a" * 100] * 1000, "chars": "a" * 100})
    return _with_examples(_calls(calls))
