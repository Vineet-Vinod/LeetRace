# Inputs are constructed within the stated limits and preserve problem-specific invariants.
import random


def generate(seed=0):
    r = random.Random(seed)
    vals = set()
    while len(vals) < 600:
        n = r.randint(1, 8)
        vals.add(tuple(r.randint(-3, 3) for _ in range(n)))
    calls = [f"candidate(nums={list(a)!r})" for a in vals]
    calls.append("candidate(nums=[-4, -3, -2, -1, 0, 1, 2, 3])")
    assert all(1 <= len(nums) <= 8 for nums in vals)
    assert all(-10 <= value <= 10 for nums in vals for value in nums)
    assert 500 <= len(calls) <= 999
    assert len(calls) == len(set(calls))
    return sorted(calls)
