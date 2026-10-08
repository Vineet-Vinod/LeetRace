def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases: set[str] = set()

    def add(grid: list[list[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        assert 2 <= rows <= 100 and 2 <= cols <= 100
        assert all(len(row) == cols for row in grid)
        assert all(value in (0, 1) for row in grid for value in row)
        cases.add(f"candidate(grid={grid!r})")

    # Odd path lengths cannot contain equal counts, including at maximum size.
    for rows, cols in [(2, 2), (3, 2), (99, 100), (100, 100)]:
        add([[rng.randrange(2) for _ in range(cols)] for _ in range(rows)])

    # On even-length paths, alternate values along a fixed monotone route to
    # guarantee a valid path, while the rest of the grid remains varied.
    for index in range(300):
        rows = 2 + index % 99
        cols = 2 + (index * 17) % 99
        if (rows + cols - 1) % 2:
            cols = 2 if cols != 2 else 3
        grid = [[rng.randrange(2) for _ in range(cols)] for _ in range(rows)]
        route = [(row, 0) for row in range(rows)] + [
            (rows - 1, col) for col in range(1, cols)
        ]
        for offset, (row, col) in enumerate(route):
            grid[row][col] = offset % 2
        add(grid)

    # Impossible parity cases and arbitrary grids broaden negatives; arbitrary
    # even-length grids provide additional positive and negative examples.
    for index in range(300):
        rows = 2 + index % 99
        cols = 2 + (index * 11) % 99
        if (rows + cols - 1) % 2 == 0:
            cols = 2 if cols != 2 else 3
        add([[rng.randrange(2) for _ in range(cols)] for _ in range(rows)])

    while len(cases) < 600:
        rows = rng.randint(2, 100)
        cols = rng.randint(2, 100)
        add([[rng.randrange(2) for _ in range(cols)] for _ in range(rows)])

    result = list(cases)
    rng.shuffle(result)
    return result
