def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        m, n = rng.randint(1, 12), rng.randint(1, 12)
        grid = [[rng.randint(1, 8) for _ in range(n)] for _ in range(m)]
        r, c = rng.randrange(m), rng.randrange(n)
        color = rng.randint(1, 1000)
        cases.add(f"candidate(grid={grid!r}, row={r}, col={c}, color={color})")
    return sorted(cases)
