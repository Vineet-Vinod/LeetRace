def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        rows, cols = rng.randint(1, 15), rng.randint(1, 15)
        grid = [[rng.choice([0, 0, 0, 1]) for _ in range(cols)] for _ in range(rows)]
        if rng.random() < 0.5:
            grid[0][0] = 0
            grid[-1][-1] = 0
        cases.add(f"candidate(obstacleGrid={grid!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]
