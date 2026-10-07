# Inputs are constructed within the stated limits and preserve problem-specific invariants.
import random


def generate(seed=0):
    r = random.Random(seed)
    vals = set()
    words = ["a", "b", "c", "D", "e", "z"]
    while len(vals) < 600:
        n = r.randint(1, 10)
        a = tuple(r.choices(words, k=n))
        b = tuple(r.choices(words, k=n))
        pairs = tuple(
            (r.choice(words), r.choice(words)) for _ in range(r.randint(0, 15))
        )
        vals.add((a, b, pairs))
    calls = [
        f"candidate(sentence1={list(a)!r}, sentence2={list(b)!r}, similarPairs={[list(p) for p in ps]!r})"
        for a, b, ps in vals
    ]
    calls.append(
        "candidate(sentence1=[chr(97+(i//676)%26)+chr(97+(i//26)%26)+chr(97+i%26) for i in range(1000)], sentence2=[chr(97+((i+1000)//676)%26)+chr(97+((i+1000)//26)%26)+chr(97+(i+1000)%26) for i in range(1000)], similarPairs=[[chr(97+(i//676)%26)+chr(97+(i//26)%26)+chr(97+i%26), chr(97+((i+1000)//676)%26)+chr(97+((i+1000)//26)%26)+chr(97+(i+1000)%26)] for i in range(1000)]*2)"
    )
    assert 500 <= len(calls) <= 999
    assert len(calls) == len(set(calls))
    return calls
