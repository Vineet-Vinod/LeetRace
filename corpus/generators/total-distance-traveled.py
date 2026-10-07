from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(mainTank=5, additionalTank=10)",
    "candidate(mainTank=1, additionalTank=2)",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(mainTank=100, additionalTank=100)")
    while len(cases) < 600:
        call = f"candidate(mainTank={rng.randint(1, 100)}, additionalTank={rng.randint(1, 100)})"
        cases.add(call)
    return sorted(cases)
