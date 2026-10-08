from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(nums=[3, 5])",
    "candidate(nums=[0, 0])",
    "candidate(nums=[0, 4, 3, 0, 4])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(nums=[1000]*100)")
    while len(cases) < 600:
        a = [rng.randint(0, 1000) for _ in range(rng.randint(1, 100))]
        call = f"candidate(nums={a!r})"
        cases.add(call)
    return sorted(cases)
