from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(columnNumber=1)",
    "candidate(columnNumber=28)",
    "candidate(columnNumber=701)",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(columnNumber=2147483647)")
    while len(cases) < 600:
        call = f"candidate(columnNumber={rng.randint(1, 2147483647)})"
        cases.add(call)
    return sorted(cases)
