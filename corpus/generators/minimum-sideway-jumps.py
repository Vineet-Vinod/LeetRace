def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 500)
        obstacles = [0] + [rng.randint(0, 3) for _ in range(n - 1)] + [0]
        cases.add(f"candidate(obstacles={obstacles!r})")
    return sorted(cases)
