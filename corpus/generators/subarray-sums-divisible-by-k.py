def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        nums = [rng.randint(-10000, 10000) for _ in range(rng.randint(1, 200))]
        k = rng.randint(2, 10000)
        cases.add(f"candidate(nums={nums!r}, k={k})")
    return sorted(cases)
