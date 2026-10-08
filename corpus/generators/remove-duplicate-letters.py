# Inputs are constructed within the stated limits and preserve problem-specific invariants.
import random


def generate(seed=0):
    r = random.Random(seed)
    vals = {"bcabc", "cbacdcbc"}
    while len(vals) < 600:
        vals.add("".join(r.choice("abcdef") for _ in range(r.randint(1, 100))))
    calls = [f"candidate(s={s!r})" for s in vals]
    calls.append(
        'candidate(s="zyxwvutsrqponmlkjihgfedcba"*384 + "zyxwvutsrqponmlkjihgfedcba"[:16])'
    )
    assert 500 <= len(calls) <= 999
    assert len(calls) == len(set(calls))
    return calls
