"""Sequence and word are nonempty lowercase strings, each at most 100 characters."""

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
    "candidate(sequence='ababc', word='ab')",
    "candidate(sequence='ababc', word='ba')",
    "candidate(sequence='ababc', word='ac')",
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
        word = "".join(rng.choice("abc") for _ in range(rng.randint(1, 6)))
        seq = "".join(rng.choice("abc") for _ in range(rng.randint(1, 50)))
        calls.append({"sequence": seq, "word": word})
    calls.append({"sequence": "a" * 100, "word": "a" * 100})
    return _with_examples(_calls(calls))
