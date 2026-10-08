def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(grid=[[1]])",
        "candidate(grid=[[1, 1], [1, 1]])",
        "candidate(grid=[[1, 1, 1], [0, 0, 1]])",
        "candidate(grid=[[1, 0], [0, 1]])",
        "candidate(grid=[[1, 1, 1], [1, 0, 1], [1, 1, 1]])",
    }

    def corridor(rows: int, cols: int) -> list[list[int]]:
        grid = [[0] * cols for _ in range(rows)]
        for col in range(cols):
            grid[0][col] = 1
        for row in range(rows):
            grid[row][cols - 1] = 1
        return grid

    def all_open(rows: int, cols: int) -> list[list[int]]:
        return [[1] * cols for _ in range(rows)]

    def closed(rows: int, cols: int) -> list[list[int]]:
        grid = [[0] * cols for _ in range(rows)]
        grid[0][0] = 1
        grid[-1][-1] = 1
        return grid

    for rows, cols in [(2, 2), (2, 3), (3, 3), (100, 1000), (1000, 100)]:
        cases.add(f"candidate(grid={corridor(rows, cols)!r})")
        cases.add(f"candidate(grid={all_open(rows, cols)!r})")
        if rows >= 3 and cols >= 3:
            cases.add(f"candidate(grid={closed(rows, cols)!r})")
    all_open_cases = set()
    while len(all_open_cases) < 300:
        rows, cols = rng.randint(2, 30), rng.randint(2, 30)
        if rows * cols > 100000:
            continue
        all_open_cases.add(f"candidate(grid={all_open(rows, cols)!r})")
    cases.update(all_open_cases)

    while len(cases) < 600:
        rows, cols = rng.randint(1, 25), rng.randint(1, 25)
        grid = [[rng.randint(0, 1) for _ in range(cols)] for _ in range(rows)]
        grid[0][0] = 1
        grid[-1][-1] = 1
        assert 1 <= rows <= 1000 and 1 <= cols <= 1000 and rows * cols <= 100000
        assert all(value in (0, 1) for row in grid for value in row)
        cases.add(f"candidate(grid={grid!r})")
    assert len(cases) == 600
    return sorted(cases)
