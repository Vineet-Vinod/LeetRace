from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(nums=[8, 1, 2, 2, 3])",
    "candidate(nums=[6, 5, 4, 8])",
    "candidate(nums=[7, 7, 7, 7])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(nums=[i%101 for i in range(500)])")
    while len(cases) < 600:
        a = [rng.randint(0, 100) for _ in range(rng.randint(2, 100))]
        call = f"candidate(nums={a!r})"
        cases.add(call)
    return sorted(cases)
