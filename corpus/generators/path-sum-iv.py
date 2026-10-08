# Inputs are constructed within the stated limits and preserve problem-specific invariants.
import random


def generate(seed=0):
    r = random.Random(seed)
    vals = set()
    while len(vals) < 600:
        root = 100 + 10 + r.randrange(10)
        left = 200 + 10 + r.randrange(10)
        right = 220 + r.randrange(10)
        vals.add(tuple(sorted((root, left, right))))
    calls = [f"candidate(nums={list(a)!r})" for a in vals]
    calls.append(
        "candidate(nums=[111, 211, 222, 311, 322, 333, 344, 411, 422, 433, 444, 455, 466, 477, 488])"
    )
    assert 500 <= len(calls) <= 999
    assert len(calls) == len(set(calls))
    return calls
