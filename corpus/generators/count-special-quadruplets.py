from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(nums=[1, 2, 3, 6])",
    "candidate(nums=[3, 3, 6, 4, 5])",
    "candidate(nums=[1, 1, 1, 3, 5])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(nums=[1]*50)")
    while len(cases) < 600:
        a = [rng.randint(1, 100) for _ in range(rng.randint(4, 10))]
        call = f"candidate(nums={a!r})"
        cases.add(call)
    return sorted(cases)
