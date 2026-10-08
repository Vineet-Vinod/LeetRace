"""Inputs contain English letters separated by spaces, include a word, and remain below length 10^4."""

import ast
import random
import string


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
    "candidate(s='Hello World')",
    "candidate(s='   fly me   to   the moon  ')",
    "candidate(s='luffy is still joyboy')",
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
                "s": " ".join(
                    "".join(
                        rng.choice(string.ascii_letters)
                        for _ in range(rng.randint(1, 12))
                    )
                    for _ in range(rng.randint(1, 10))
                )
                + " " * rng.randint(0, 3)
            }
        )
    calls.append({"s": "a" * 10_000})
    return _with_examples(_calls(calls))
