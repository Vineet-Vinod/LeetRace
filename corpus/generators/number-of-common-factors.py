from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = ["candidate(a=12, b=6)", "candidate(a=25, b=30)"]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(a=1000, b=1000)")
    while len(cases) < 600:
        call = f"candidate(a={rng.randint(1, 1000)}, b={rng.randint(1, 1000)})"
        cases.add(call)
    return sorted(cases)
