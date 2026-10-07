def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        m, n = 2 * rng.randint(1, 25), 2 * rng.randint(1, 25)
        grid = [[rng.randint(1, 5000) for _ in range(n)] for _ in range(m)]
        k = rng.randint(1, 10**9)
        cases.add(f"candidate(grid={grid!r}, k={k})")
    return sorted(cases)
