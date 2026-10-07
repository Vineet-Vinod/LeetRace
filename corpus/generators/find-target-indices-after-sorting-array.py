from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(nums=[1, 2, 5, 2, 3], target=2)",
    "candidate(nums=[1, 2, 5, 2, 3], target=3)",
    "candidate(nums=[1, 2, 5, 2, 3], target=5)",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(nums=[100]*100, target=100)")
    while len(cases) < 600:
        a = [rng.randint(1, 100) for _ in range(rng.randint(1, 100))]
        t = rng.randint(1, 100)
        call = f"candidate(nums={a!r}, target={t})"
        cases.add(call)
    return sorted(cases)
