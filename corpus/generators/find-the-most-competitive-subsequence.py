def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = {"candidate(nums=[3,5,2,6], k=2)"}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        nums = [rng.randint(0, 10**9) for _ in range(n)]
        k = rng.randint(1, n)
        cases.add(f"candidate(nums={nums!r}, k={k})")
    return sorted(cases)
