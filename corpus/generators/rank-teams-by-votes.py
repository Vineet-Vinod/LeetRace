# Inputs are constructed within the stated limits and preserve problem-specific invariants.
import random


def generate(seed=0):
    r = random.Random(seed)
    vals = set()
    alphabet = "ABCDEFGH"
    while len(vals) < 600:
        n = r.randint(1, 8)
        teams = "".join(r.sample(alphabet, n))
        k = r.randint(1, 20)
        vals.add(tuple("".join(r.sample(teams, n)) for _ in range(k)))
    calls = [f"candidate(votes={list(v)!r})" for v in vals]
    calls.append(
        'candidate(votes=["ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i%26:]+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:i%26] for i in range(1000)])'
    )
    assert 500 <= len(calls) <= 999
    assert len(calls) == len(set(calls))
    return calls
