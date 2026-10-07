from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = ["candidate(n=13)", "candidate(n=2)"]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(n=1)")
    cases.add("candidate(n=9999)")
    cases.add("candidate(n=10000)")
    while len(cases) < 600:
        call = f"candidate(n={rng.randint(1, 10000)})"
        cases.add(call)
    return sorted(cases)
