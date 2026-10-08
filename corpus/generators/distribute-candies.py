from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(candyType=[1, 1, 2, 2, 3, 3])",
    "candidate(candyType=[1, 1, 2, 3])",
    "candidate(candyType=[6, 6, 6, 6])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(candyType=[1]*10000)")
    cases.add("candidate(candyType=[-100000,100000]*5000)")
    while len(cases) < 600:
        n = 2 * rng.randint(1, 50)
        a = [rng.randint(-100000, 100000) for _ in range(n)]
        call = f"candidate(candyType={a!r})"
        cases.add(call)
    return sorted(cases)
