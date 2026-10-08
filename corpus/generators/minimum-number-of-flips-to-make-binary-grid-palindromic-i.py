def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(grid=[[1, 0, 0], [0, 0, 0], [0, 0, 1]])",
        "candidate(grid=[[0, 1], [0, 1], [0, 0]])",
        "candidate(grid=[[1], [0]])",
        "candidate(grid=[[1, 0, 1, 1]])",
        "candidate(grid=[[1], [0], [1], [1]])",
        "candidate(grid=[[1, 1, 0], [0, 1, 0], [0, 1, 1]])",
        "candidate(grid=[[1, 0, 1], [1, 1, 0]])",
        "candidate(grid=[[1, 0, 0, 1], [0, 1, 1, 0], [1, 0, 1, 0]])",
        "candidate(grid=[[1, 0, 1, 0], [0, 1, 0, 1]])",
        "candidate(grid=[[1, 1, 0, 0, 1], [0, 0, 1, 1, 0], [1, 0, 1, 0, 1]])",
        "candidate(grid=[[1, 0, 1], [0, 1, 0], [1, 0, 1]])",
        f"candidate(grid={[[rng.randrange(2) for _ in range(200000)]]!r})",
    }
    while len(cases) < 600:
        rows, columns = rng.randint(1, 100), rng.randint(1, 100)
        grid = [[rng.randrange(2) for _ in range(columns)] for _ in range(rows)]
        assert 1 <= rows * columns <= 200_000
        assert all(value in (0, 1) for row in grid for value in row)
        cases.add(f"candidate(grid={grid!r})")
    return sorted(cases)
