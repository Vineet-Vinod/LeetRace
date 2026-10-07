def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 10)
        arr = list(range(n))
        rng.shuffle(arr)
        cases.add(f"candidate(arr={arr!r})")
    return sorted(cases)
