# Inputs are constructed within the stated limits and preserve problem-specific invariants.
import random


def generate(seed=0):
    r = random.Random(seed)
    vals = set()
    while len(vals) < 600:
        n = r.randint(3, 30)
        edges = [(i, i + 1) for i in range(1, n)] + [(1, n)]
        r.shuffle(edges)
        vals.add(tuple(edges))
    calls = [f"candidate(edges={[list(e) for e in a]!r})" for a in vals]
    calls.append("candidate(edges=[[i, i+1] for i in range(1,1000)]+[[1,1000]])")
    assert 500 <= len(calls) <= 999
    assert len(calls) == len(set(calls))
    return calls
