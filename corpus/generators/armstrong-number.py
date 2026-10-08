"""Enumerates digit multisets for each digit count 1..9, so every positive Armstrong number up to 10^8 is included; seeded nonexamples exercise the false branch."""

import ast
import random
from itertools import combinations_with_replacement


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


def positive_armstrong_numbers() -> list[int]:
    values: set[int] = set()
    for digit_count in range(1, 10):
        for digits in combinations_with_replacement(range(10), digit_count):
            value = sum(digit**digit_count for digit in digits)
            if value == 0 or value > 100_000_000 or len(str(value)) != digit_count:
                continue
            if tuple(sorted(int(char) for char in str(value))) == digits:
                values.add(value)
    return sorted(values)


EXAMPLE_CALLS = ["candidate(n=153)", "candidate(n=123)"]


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
    values = positive_armstrong_numbers()
    assert len(values) == len(set(values))
    assert all(
        sum(int(digit) ** len(str(value)) for digit in str(value)) == value
        for value in values
    )
    values.extend([10, 99_999_999, 100_000_000])
    values.extend(rng.randint(1, 100_000_000) for _ in range(600))
    calls = _calls([{"n": value} for value in values])
    assert all(
        f"candidate(n={value})" in calls for value in positive_armstrong_numbers()
    )
    return _with_examples(calls)
