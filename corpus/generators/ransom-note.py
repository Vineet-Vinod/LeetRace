"""Both lowercase strings are nonempty and at most 100 characters; independently generated strings cover possible and impossible constructions."""

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
    "candidate(ransomNote='a', magazine='b')",
    "candidate(ransomNote='aa', magazine='ab')",
    "candidate(ransomNote='aa', magazine='aab')",
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
        magazine = "".join(rng.choice("abcdef") for _ in range(rng.randint(1, 100)))
        note = "".join(rng.choice("abcdef") for _ in range(rng.randint(1, 100)))
        calls.append({"ransomNote": note, "magazine": magazine})
    calls.append({"ransomNote": "a" * 100_000, "magazine": "a" * 100_000})
    return _with_examples(_calls(calls))
