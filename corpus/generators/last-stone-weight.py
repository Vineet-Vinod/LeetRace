from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = ["candidate(stones=[2, 7, 4, 1, 8, 1])", "candidate(stones=[1])"]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(stones=[1000]*30)")
    while len(cases) < 600:
        a = [rng.randint(1, 1000) for _ in range(rng.randint(1, 30))]
        call = f"candidate(stones={a!r})"
        cases.add(call)
    return sorted(cases)
