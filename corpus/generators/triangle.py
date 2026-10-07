def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 100)
        triangle = [
            [rng.randint(-10000, 10000) for _ in range(row + 1)] for row in range(n)
        ]
        cases.add(f"candidate(triangle={triangle!r})")
    return sorted(cases)
