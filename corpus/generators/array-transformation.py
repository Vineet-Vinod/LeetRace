from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = ["candidate(arr=[6, 2, 3, 4])", "candidate(arr=[1, 6, 3, 4, 3, 5])"]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(arr=list(range(1,101)))")
    while len(cases) < 600:
        n = rng.randint(3, 30)
        a = [rng.randint(1, 100) for _ in range(n)]
        call = f"candidate(arr={a!r})"
        cases.add(call)
    return sorted(cases)
