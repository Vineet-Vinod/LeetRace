# Inputs are constructed within the stated limits and preserve problem-specific invariants.
import random


def generate(seed: int = 0) -> list[str]:
    r = random.Random(seed)
    vals = {(1, 0), (5, 0), (19, 2), (10, 4), (10**9, 100)}
    while len(vals) < 600:
        vals.add((r.randint(1, 10**9), r.randint(0, 100)))
    calls = [f"candidate(target={a}, maxDoubles={b})" for a, b in sorted(vals)]
    assert 500 <= len(calls) <= 999
    assert len(calls) == len(set(calls))
    return calls
