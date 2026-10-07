def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        r, c = rng.randint(1, 15), rng.randint(1, 15)
        grid = [[rng.randint(1, 1000) for _ in range(c)] for _ in range(r)]
        cases.add(f"candidate(grid={grid!r})")
    return sorted(cases)
