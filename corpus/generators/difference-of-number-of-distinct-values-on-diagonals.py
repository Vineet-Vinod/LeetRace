def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        m, n = rng.randint(1, 50), rng.randint(1, 50)
        grid = [[rng.randint(1, 50) for _ in range(n)] for _ in range(m)]
        cases.add(f"candidate(grid={grid!r})")
    return sorted(cases)
