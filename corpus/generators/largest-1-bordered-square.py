def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        m, n = rng.randint(1, 100), rng.randint(1, 100)
        grid = [[rng.randint(0, 1) for _ in range(n)] for _ in range(m)]
        cases.add(f"candidate(grid={grid!r})")
    return sorted(cases)
