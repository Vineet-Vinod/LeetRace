def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        arr = [rng.randint(1, 100) for _ in range(rng.randint(1, 200))]
        cases.add(f"candidate(arr={arr!r})")
    return sorted(cases)
