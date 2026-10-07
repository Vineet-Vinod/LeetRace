"""num is sampled from 0..10^6 and includes the exact upper bound, powers of ten, and nonzero last digits."""

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


EXAMPLE_CALLS = ["candidate(num=526)", "candidate(num=1800)", "candidate(num=0)"]


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
    values = [0, 1, 10, 100, 526, 1800, 1000000]
    values += [rng.randrange(0, 1_000_001) for _ in range(600)]
    return _with_examples(_calls([{"num": n} for n in values]))
