"""Letters are sorted lowercase characters with at least two distinct values; target is lowercase."""

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
    "candidate(letters=['c', 'f', 'j'], target='a')",
    "candidate(letters=['c', 'f', 'j'], target='c')",
    "candidate(letters=['x', 'x', 'y', 'y'], target='z')",
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
        letters = sorted(
            set(rng.sample(list(string.ascii_lowercase), rng.randint(2, 15)))
        )
        calls.append({"letters": letters, "target": rng.choice(string.ascii_lowercase)})
    calls.append({"letters": ["a"] * 9_999 + ["z"], "target": "y"})
    return _with_examples(_calls(calls))
