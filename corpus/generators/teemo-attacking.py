from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(timeSeries=[1, 4], duration=2)",
    "candidate(timeSeries=[1, 2], duration=2)",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(timeSeries=list(range(10000)), duration=10000000)")
    while len(cases) < 600:
        n = rng.randint(1, 1000)
        a = sorted(rng.randint(0, 100000) for _ in range(n))
        d = rng.randint(0, 10000000)
        call = f"candidate(timeSeries={a!r}, duration={d})"
        cases.add(call)
    return sorted(cases)
