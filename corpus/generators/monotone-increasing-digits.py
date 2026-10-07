# Inputs are constructed within the stated limits and preserve problem-specific invariants.
import random


def generate(seed: int = 0) -> list[str]:
    r = random.Random(seed)
    vals = {0, 10, 1234, 332, 10**9}
    while len(vals) < 600:
        vals.add(r.randint(0, 10**9))
    calls = [f"candidate(n={n})" for n in sorted(vals)]
    assert 500 <= len(calls) <= 999
    assert len(calls) == len(set(calls))
    return calls
