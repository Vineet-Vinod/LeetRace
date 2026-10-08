# Inputs are constructed within the stated limits and preserve problem-specific invariants.
import random


def generate(seed=0):
    r = random.Random(seed)
    vals = set()
    while len(vals) < 600:
        n = r.randint(2, 40)
        edges = {
            tuple(sorted((i, r.randrange(i)))) for i in range(1, n) if r.random() < 0.6
        }
        possible = [
            (a, b) for a in range(n) for b in range(a + 1, n) if (a, b) not in edges
        ]
        for _ in range(r.randint(0, min(20, len(possible)))):
            if possible:
                edges.add(possible.pop(r.randrange(len(possible))))
        if not edges:
            edges.add((0, 1))
        vals.add((n, tuple(sorted(edges))))
    calls = [
        f"candidate(n={n}, connections={[list(e) for e in es]!r})" for n, es in vals
    ]
    calls.append("candidate(n=100000, connections=[[i, i+1] for i in range(99999)])")
    assert 500 <= len(calls) <= 999
    assert len(calls) == len(set(calls))
    return calls
