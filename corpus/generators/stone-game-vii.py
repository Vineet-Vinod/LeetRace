def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        stones = [rng.randint(1, 1000) for _ in range(rng.randint(2, 100))]
        cases.add(f"candidate(stones={stones!r})")
    return sorted(cases)
