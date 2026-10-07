from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(nums=[-2, -1, -1, 1, 2, 3])",
    "candidate(nums=[-3, -2, -1, 0, 0, 1, 2])",
    "candidate(nums=[5, 20, 66, 1314])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(nums=list(range(-1000,1000)))")
    cases.add("candidate(nums=[-2000]+list(range(-1999,0)) )")
    cases.add("candidate(nums=list(range(-1998,1))+[2000])")
    while len(cases) < 600:
        a = sorted(rng.randint(-100, 100) for _ in range(rng.randint(1, 100)))
        call = f"candidate(nums={a!r})"
        cases.add(call)
    return sorted(cases)
