def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        x, y = rng.randint(1, 10**4), rng.randint(1, 10**4)
        cases.add(f"candidate(x={x}, y={y})")
    return sorted(cases)
