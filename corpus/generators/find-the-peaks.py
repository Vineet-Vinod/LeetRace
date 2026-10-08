from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = ["candidate(mountain=[2, 4, 4])", "candidate(mountain=[1, 4, 3, 8, 5])"]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(mountain=list(range(1,101)))")
    while len(cases) < 600:
        n = rng.randint(3, 100)
        a = []
        for _ in range(n):
            a.append(rng.choice([v for v in range(1, 101) if not a or v != a[-1]]))
        call = f"candidate(mountain={a!r})"
        cases.add(call)
    return sorted(cases)
