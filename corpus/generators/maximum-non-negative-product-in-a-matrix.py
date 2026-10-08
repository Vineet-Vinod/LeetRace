import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], ...]] = {
        ((-1, -2, -3), (-2, -3, -3), (-3, -3, -2)),
        ((1, -2, 1), (1, -2, 1), (3, -4, 1)),
        ((1, 3), (0, -4)),
        ((0,),),
        ((-4,),),
    }
    cases.add(tuple(tuple(1 for _ in range(15)) for _ in range(15)))
    while len(cases) < 600:
        rows, cols = rng.randint(1, 8), rng.randint(1, 8)
        cases.add(
            tuple(tuple(rng.randint(-4, 4) for _ in range(cols)) for _ in range(rows))
        )
    assert all(
        1 <= len(grid) <= 15
        and 1 <= len(grid[0]) <= 15
        and all(
            len(row) == len(grid[0]) and all(-4 <= value <= 4 for value in row)
            for row in grid
        )
        for grid in cases
    )
    return [
        f"candidate(grid={[list(row) for row in grid]!r})" for grid in sorted(cases)
    ]
