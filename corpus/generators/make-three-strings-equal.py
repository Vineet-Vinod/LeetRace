from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(s1='abc', s2='abb', s3='ab')",
    "candidate(s1='dac', s2='bac', s3='cac')",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(s1='a'*100, s2='a'*100, s3='a'*100)")
    while len(cases) < 600:
        a = [
            "".join(rng.choice("abc") for _ in range(rng.randint(1, 10)))
            for _ in range(3)
        ]
        call = f"candidate(s1={a[0]!r}, s2={a[1]!r}, s3={a[2]!r})"
        cases.add(call)
    return sorted(cases)
