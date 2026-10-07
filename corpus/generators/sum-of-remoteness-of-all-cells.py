def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(grid=[[-1, 1, -1], [5, -1, 4], [-1, 3, -1]])",
        "candidate(grid=[[-1, 3, 4], [-1, -1, -1], [3, -1, -1]])",
        "candidate(grid=[[1]])",
        f"candidate(grid={[[1] * 300 for _ in range(300)]!r})",
    }
    while len(cases) < 600:
        n = rng.randint(1, 10)
        grid = [
            [-1 if rng.random() < 0.35 else rng.randint(1, 1000000) for _ in range(n)]
            for _ in range(n)
        ]
        assert 1 <= n <= 300 and all(
            x == -1 or 1 <= x <= 1000000 for row in grid for x in row
        )
        cases.add(f"candidate(grid={grid!r})")
    return sorted(cases)
