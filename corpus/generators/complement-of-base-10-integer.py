"""n is in [0,10^9); includes zero and values near the upper bound."""

import ast
import random


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


EXAMPLE_CALLS = ["candidate(n=5)", "candidate(n=7)", "candidate(n=10)"]


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
    values = [0, 1, 2, 5, 7, 10, 511, 512, 999_999_999]
    values += [rng.randint(0, 999_999_999) for _ in range(620)]
    return _with_examples(_calls([{"n": n} for n in values]))
