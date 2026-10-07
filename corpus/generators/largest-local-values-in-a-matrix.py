from __future__ import annotations
import random

# Inputs stay within the written constraints; semantic preconditions are built into each case.
EXAMPLE_CALLS = [
    "candidate(grid=[[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]])",
    "candidate(grid=[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)

    def add(grid: list[list[int]]) -> None:
        assert 3 <= len(grid) <= 100
        assert all(len(row) == len(grid) for row in grid)
        assert all(1 <= value <= 100 for row in grid for value in row)
        cases.add(f"candidate(grid={grid!r})")

    add([[100 - (index % 100) for index in range(100)] for _ in range(100)])
    add([[index % 100 + 1 for index in range(100)] for _ in range(100)])
    while len(cases) < 600:
        n = rng.randint(3, 10)
        grid = [[rng.randint(1, 100) for _ in range(n)] for _ in range(n)]
        add(grid)
    for call in cases:
        eval(call, {"candidate": lambda grid: add(grid)})
    return sorted(cases)
