from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]])",
    "candidate(grid=[[1]])",
    "candidate(grid=[[1, 0]])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)
    cases.add("candidate(grid=[[1]*100 for _ in range(100)])")
    cases.add("candidate(grid=[[1]*100 for _ in range(100)])")
    while len(cases) < 600:
        m = rng.randint(1, 10)
        n = rng.randint(1, 10)
        a = [
            [int(rng.random() < 0.55) for _ in range(n)] for _ in range(m)
        ]  # one valid connected island: solid random rectangle
        h = rng.randint(1, m)
        w = rng.randint(1, n)
        y = rng.randint(0, m - h)
        x = rng.randint(0, n - w)
        a = [
            [int(y <= i < y + h and x <= j < x + w) for j in range(n)] for i in range(m)
        ]
        call = f"candidate(grid={a!r})"
        cases.add(call)
    return sorted(cases)
