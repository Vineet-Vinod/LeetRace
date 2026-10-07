from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(s='iiii', k=1)",
    "candidate(s='leetcode', k=2)",
    "candidate(s='zbax', k=2)",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(s='z'*100, k=10)")
    while len(cases) < 600:
        a = "".join(
            rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(rng.randint(1, 100))
        )
        k = rng.randint(1, 10)
        call = f"candidate(s={a!r}, k={k})"
        cases.add(call)
    return sorted(cases)
