def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        n = rng.randint(1, 100)
        nums = [rng.randint(1, 10**6) for _ in range(n)]
        k = rng.randint(0, n - 1)
        cases.add(f"candidate(nums={nums!r}, k={k})")
    return sorted(cases)
