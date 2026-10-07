# Inputs are constructed within the stated limits and preserve problem-specific invariants.
import random


def generate(seed=0):
    r = random.Random(seed)
    vals = {(4, 2), (3, 1), (30, 7), (1000, 999)}
    while len(vals) < 600:
        n = r.randint(2, 1000)
        vals.add((n, r.randint(1, n - 1)))
    calls = [f"candidate(n={n}, k={k})" for n, k in vals]
    assert 500 <= len(calls) <= 999
    assert len(calls) == len(set(calls))
    return calls
