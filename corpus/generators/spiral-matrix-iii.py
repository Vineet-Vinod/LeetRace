# Inputs are constructed within the stated limits and preserve problem-specific invariants.
import random


def generate(seed=0):
    r = random.Random(seed)
    vals = {(100, 100, 0, 0)}
    while len(vals) < 600:
        rows = r.randint(1, 30)
        cols = r.randint(1, 30)
        rs = r.randrange(rows)
        cs = r.randrange(cols)
        vals.add((rows, cols, rs, cs))
    calls = [
        f"candidate(rows={a}, cols={b}, rStart={c}, cStart={d})" for a, b, c, d in vals
    ]
    assert 500 <= len(calls) <= 999
    assert len(calls) == len(set(calls))
    return calls
