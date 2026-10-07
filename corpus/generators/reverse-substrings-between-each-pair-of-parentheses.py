# Inputs are constructed within the stated limits and preserve problem-specific invariants.
import random


def generate(seed=0):
    r = random.Random(seed)
    vals = {"(abcd)", "(u(love)i)", "(ed(et(oc))el)"}
    while len(vals) < 600:
        n = r.randint(1, 60)
        s = ""
        depth = 0
        for _ in range(n):
            if depth and r.random() < 0.15:
                s += ")"
                depth -= 1
            elif r.random() < 0.15:
                s += "("
                depth += 1
            else:
                s += r.choice("abcde")
        s += ")" * depth
        vals.add(s)
    calls = [f"candidate(s={s!r})" for s in vals]
    calls.append('candidate(s="("*999+"ab"+")"*999)')
    assert 500 <= len(calls) <= 999
    assert len(calls) == len(set(calls))
    return calls
