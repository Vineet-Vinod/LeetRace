"""Nonempty printable-ASCII strings have length at most 2*10^5; 250 constructed palindromes exercise the true branch and one case hits the length bound."""

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
    "candidate(s='A man, a plan, a canal: Panama')",
    "candidate(s='race a car')",
    "candidate(s=' ')",
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
                "s": "".join(
                    rng.choice(string.ascii_letters + string.digits + " ,.!?")
                    for _ in range(rng.randint(1, 100))
                )
            }
        )
    for _ in range(250):
        half = "".join(
            rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 20))
        )
        center = rng.choice(string.ascii_lowercase)
        calls.append({"s": half + center + half[::-1]})
    calls.append({"s": "a" * 200_000})
    return _with_examples(_calls(calls))
