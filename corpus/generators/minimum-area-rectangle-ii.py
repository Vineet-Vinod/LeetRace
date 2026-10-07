def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        points = set()
        while len(points) < rng.randint(1, 20):
            points.add((rng.randint(0, 40000), rng.randint(0, 40000)))
        cases.add(f"candidate(points={[list(p) for p in points]!r})")
    return sorted(cases)
