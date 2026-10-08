from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = ["candidate(num=38)", "candidate(num=0)"]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(num=0)")
    cases.add("candidate(num=9)")
    cases.add("candidate(num=10)")
    cases.add("candidate(num=2147483647)")
    while len(cases) < 600:
        call = f"candidate(num={rng.randint(0, 2_147_483_647)})"
        cases.add(call)
    return sorted(cases)
