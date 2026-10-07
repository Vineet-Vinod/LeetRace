def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        r, c = rng.randint(1, 15), rng.randint(1, 15)
        x = rng.randint(1, 100)
        base = rng.randint(1, 1000)
        grid = [[base + x * rng.randint(0, 20) for _ in range(c)] for _ in range(r)]
        cases.add(f"candidate(grid={grid!r},x={x})")
    return sorted(cases)
