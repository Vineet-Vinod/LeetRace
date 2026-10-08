def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        props = [
            [rng.randint(1, 10**5), rng.randint(1, 10**5)]
            for _ in range(rng.randint(2, 100))
        ]
        cases.add(f"candidate(properties={props!r})")
    return sorted(cases)
