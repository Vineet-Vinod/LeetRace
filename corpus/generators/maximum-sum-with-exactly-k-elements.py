from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(nums=[1, 2, 3, 4, 5], k=3)",
    "candidate(nums=[5, 5, 5], k=2)",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(nums=[100]*100, k=100)")
    while len(cases) < 600:
        a = [rng.randint(1, 100) for _ in range(rng.randint(1, 100))]
        k = rng.randint(1, 100)
        call = f"candidate(nums={a!r}, k={k})"
        cases.add(call)
    return sorted(cases)
