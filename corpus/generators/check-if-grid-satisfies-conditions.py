from __future__ import annotations
import random

EXAMPLE_CALLS = [
    "candidate(grid=[[1, 0, 2], [1, 0, 2]])",
    "candidate(grid=[[1, 1, 1], [0, 0, 0]])",
    "candidate(grid=[[1], [2], [3]])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    valid = {EXAMPLE_CALLS[0], "candidate(grid=[list(range(10)) for _ in range(10)])"}
    invalid = set(EXAMPLE_CALLS[1:])
    invalid.add("candidate(grid=[[0]*10, [1]*10]+[[0]*10 for _ in range(8)])")
    while len(valid) < 300:
        rows = rng.randint(1, 10)
        columns = rng.randint(1, 10)
        values = rng.sample(range(10), columns)
        grid = [values[:] for _ in range(rows)]
        valid.add(f"candidate(grid={grid!r})")
    while len(invalid) < 300:
        rows = rng.randint(1, 10)
        columns = rng.randint(2, 10) if rows == 1 else rng.randint(1, 10)
        grid = [[rng.randint(0, 9) for _ in range(columns)] for _ in range(rows)]
        if rows > 1:
            grid[0][0], grid[1][0] = 0, 1
        else:
            grid[0][0] = grid[0][1] = 0
        invalid.add(f"candidate(grid={grid!r})")
    assert len(valid) == 300 and len(invalid) == 300
    return sorted(valid | invalid)
