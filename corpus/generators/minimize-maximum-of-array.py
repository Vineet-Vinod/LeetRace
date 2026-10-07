def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        nums = [rng.randint(0, 10**9) for _ in range(rng.randint(2, 150))]
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
