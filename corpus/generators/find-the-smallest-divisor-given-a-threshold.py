def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = {"candidate(nums=[1,2,5,9], threshold=6)"}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        nums = [rng.randint(1, 10**6) for _ in range(n)]
        threshold = rng.randint(n, 10**6)
        cases.add(f"candidate(nums={nums!r}, threshold={threshold})")
    return sorted(cases)
