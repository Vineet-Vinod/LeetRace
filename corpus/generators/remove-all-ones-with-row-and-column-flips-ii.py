def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        m = rng.randint(1, 15)
        n = rng.randint(1, 15)
        n = min(n, 15 // m)
        grid = [[rng.randint(0, 1) for _ in range(n)] for _ in range(m)]
        cases.add(f"candidate(grid={grid!r})")
    return sorted(cases)
