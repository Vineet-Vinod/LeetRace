def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        r, c = rng.randint(1, 30), rng.randint(1, 30)
        grid = [[rng.randrange(2) for _ in range(c)] for _ in range(r)]
        if not any(map(any, grid)):
            grid[rng.randrange(r)][rng.randrange(c)] = 1
        cases.add(f"candidate(grid={grid!r})")
    return sorted(cases)
