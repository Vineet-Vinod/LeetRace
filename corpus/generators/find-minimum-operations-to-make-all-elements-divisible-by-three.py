from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = ["candidate(nums=[1, 2, 3, 4])", "candidate(nums=[3, 6, 9])"]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(nums=[50]*50)")
    while len(cases) < 600:
        a = [rng.randint(1, 50) for _ in range(rng.randint(1, 50))]
        call = f"candidate(nums={a!r})"
        cases.add(call)
    return sorted(cases)
