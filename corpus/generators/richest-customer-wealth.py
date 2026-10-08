from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(accounts=[[1, 2, 3], [3, 2, 1]])",
    "candidate(accounts=[[1, 5], [7, 3], [3, 5]])",
    "candidate(accounts=[[2, 8, 7], [7, 1, 3], [1, 9, 5]])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(accounts=[[100]*50 for _ in range(50)])")
    while len(cases) < 600:
        m = rng.randint(1, 50)
        n = rng.randint(1, 50)
        a = [[rng.randint(1, 100) for _ in range(n)] for _ in range(m)]
        call = f"candidate(accounts={a!r})"
        cases.add(call)
    return sorted(cases)
