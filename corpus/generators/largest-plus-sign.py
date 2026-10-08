def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = {"candidate(n=1, mines=[[0, 0]])"}
    while len(cases) < 600:
        n = rng.randint(1, 50)
        positions = set()
        while len(positions) < rng.randint(1, min(100, n * n)):
            positions.add((rng.randrange(n), rng.randrange(n)))
        mines = [list(pair) for pair in positions]
        cases.add(f"candidate(n={n}, mines={mines!r})")
    return sorted(cases)
