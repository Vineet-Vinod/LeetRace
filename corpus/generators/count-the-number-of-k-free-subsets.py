def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 50)
        nums = sorted(rng.sample(range(1, 1001), n))
        k = rng.randint(1, 1000)
        cases.add(f"candidate(nums={nums!r}, k={k})")
    return sorted(cases)
