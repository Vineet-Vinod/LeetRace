def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        m, n = rng.randint(2, 10), rng.randint(2, 10)
        vals = list(range(m * n))
        rng.shuffle(vals)
        grid = [vals[r * n : (r + 1) * n] for r in range(m)]
        costs = [[rng.randint(1, 100) for _ in range(n)] for _ in range(m * n)]
        cases.add(f"candidate(grid={grid!r}, moveCost={costs!r})")
    return sorted(cases)
