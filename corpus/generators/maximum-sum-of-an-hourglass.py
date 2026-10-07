import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], ...]] = {
        ((6, 2, 1, 3), (4, 2, 1, 5), (9, 2, 8, 7), (4, 1, 2, 9)),
        ((1, 2, 3), (4, 5, 6), (7, 8, 9)),
        ((0, 0, 0), (0, 0, 0), (0, 0, 0)),
        tuple(tuple(1_000_000 for _ in range(150)) for _ in range(150)),
    }
    while len(cases) < 600:
        rows, cols = rng.randint(3, 20), rng.randint(3, 20)
        cases.add(
            tuple(
                tuple(rng.randint(0, 1_000_000) for _ in range(cols))
                for _ in range(rows)
            )
        )
    assert all(
        3 <= len(grid) <= 150
        and 3 <= len(grid[0]) <= 150
        and all(
            len(row) == len(grid[0]) and all(0 <= value <= 1_000_000 for value in row)
            for row in grid
        )
        for grid in cases
    )
    return [
        f"candidate(grid={[list(row) for row in grid]!r})" for grid in sorted(cases)
    ]
