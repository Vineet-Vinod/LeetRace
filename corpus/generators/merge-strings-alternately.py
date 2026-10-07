"""Both input strings are nonempty lowercase strings and each has length at most 100."""

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
    "candidate(word1='abc', word2='pqr')",
    "candidate(word1='ab', word2='pqrs')",
    "candidate(word1='abcd', word2='pq')",
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
                "word1": "".join(rng.choice("abc") for _ in range(rng.randint(1, 100))),
                "word2": "".join(rng.choice("xyz") for _ in range(rng.randint(1, 100))),
            }
        )
    calls.append({"word1": "a" * 100, "word2": "b" * 100})
    return _with_examples(_calls(calls))
