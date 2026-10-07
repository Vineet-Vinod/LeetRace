# Inputs are constructed within the stated limits and preserve problem-specific invariants.
import random


def generate(seed: int = 0) -> list[str]:
    r = random.Random(seed)
    vals = set()
    for m, n in [(1, 1), (1, 1000), (1000, 1), (2, 3), (3, 4)]:
        vals.add(tuple(tuple(r.randrange(10) for _ in range(n)) for _ in range(m)))
    while len(vals) < 600:
        m = r.randint(1, 6)
        n = r.randint(1, 6)
        vals.add(tuple(tuple(r.randrange(10) for _ in range(n)) for _ in range(m)))
    calls = [f"candidate(grid={[list(row) for row in g]!r})" for g in vals]
    calls.append("candidate(grid=[[0]*1000 for _ in range(1000)])")
    assert 500 <= len(calls) <= 999
    assert len(calls) == len(set(calls))
    return calls
