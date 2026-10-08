from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(n=4, rounds=[1, 3, 1, 2])",
    "candidate(n=2, rounds=[2, 1, 2, 1, 2, 1, 2, 1, 2])",
    "candidate(n=7, rounds=[1, 3, 5, 7])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(n=2, rounds=[1,2]*50+[1])")
    while len(cases) < 600:
        n = rng.randint(2, 100)
        rounds = [rng.randint(1, n)]
        for _ in range(rng.randint(1, 99)):
            rounds.append(rng.choice([x for x in range(1, n + 1) if x != rounds[-1]]))
        call = f"candidate(n={n}, rounds={rounds!r})"
        cases.add(call)
    return sorted(cases)
