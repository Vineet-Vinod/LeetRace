from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(grid=[[0, 1], [0, 0]])",
    "candidate(grid=[[0, 0, 1], [1, 0, 1], [0, 0, 0]])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(grid=[[int(i<j) for j in range(100)] for i in range(100)])")
    while len(cases) < 600:
        n = rng.randint(2, 20)
        order = list(range(n))
        rng.shuffle(order)
        a = [
            [int(order[i] < order[j]) if i != j else 0 for j in range(n)]
            for i in range(n)
        ]
        call = f"candidate(grid={a!r})"
        cases.add(call)
    return sorted(cases)
