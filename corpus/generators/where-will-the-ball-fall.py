# Inputs are constructed within the stated limits and preserve problem-specific invariants.
import random


def generate(seed=0):
    r = random.Random(seed)
    vals = {tuple(tuple(1 for _ in range(100)) for _ in range(100))}
    while len(vals) < 600:
        m = r.randint(1, 15)
        n = r.randint(1, 15)
        vals.add(tuple(tuple(r.choice((-1, 1)) for _ in range(n)) for _ in range(m)))
    calls = [f"candidate(grid={[list(row) for row in g]!r})" for g in vals]
    assert 500 <= len(calls) <= 999
    assert len(calls) == len(set(calls))
    return calls
