def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        nums = [rng.randint(1, 10**6) for _ in range(rng.randint(2, 200))]
        x = rng.randint(1, 10**6)
        cases.add(f"candidate(nums={nums!r}, x={x})")
    return sorted(cases)
