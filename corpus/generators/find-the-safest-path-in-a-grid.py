import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], ...]] = {
        ((0, 0, 1), (0, 0, 0), (0, 0, 0)),
        ((0, 0, 0, 1), (0, 0, 0, 0), (0, 0, 0, 0), (1, 0, 0, 0)),
        ((1,),),
    }
    size = 400
    grid = [[0] * size for _ in range(size)]
    grid[size // 2][size // 2] = 1
    cases.add(tuple(tuple(row) for row in grid))
    while len(cases) < 600:
        size = rng.randint(1, 20)
        grid = [[0] * size for _ in range(size)]
        for _ in range(rng.randint(1, max(1, size * size // 4))):
            grid[rng.randrange(size)][rng.randrange(size)] = 1
        cases.add(tuple(tuple(row) for row in grid))
    assert all(
        1 <= len(grid) <= 400
        and all(len(row) == len(grid) for row in grid)
        and any(value == 1 for row in grid for value in row)
        and all(value in (0, 1) for row in grid for value in row)
        for grid in cases
    )
    return [
        f"candidate(grid={[list(row) for row in grid]!r})" for grid in sorted(cases)
    ]
