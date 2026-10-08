from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = ["candidate(nums=[4, 3, 10, 9, 8])", "candidate(nums=[4, 4, 7, 6, 7])"]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(nums=[100]*500)")
    while len(cases) < 600:
        a = [rng.randint(1, 100) for _ in range(rng.randint(1, 500))]
        call = f"candidate(nums={a!r})"
        cases.add(call)
    return sorted(cases)
