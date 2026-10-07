# Inputs are constructed within the stated limits and preserve problem-specific invariants.
import random


def generate(seed=0):
    r = random.Random(seed)
    vals = {12, 21, 12443322, 1999999999, 2147483476, 2**31 - 1}
    while len(vals) < 600:
        vals.add(r.randint(1, 2**31 - 1))
    calls = [f"candidate(n={x})" for x in sorted(vals)]
    assert 500 <= len(calls) <= 999
    assert len(calls) == len(set(calls))
    return calls
