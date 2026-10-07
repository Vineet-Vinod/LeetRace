def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = set()
    cases.add("candidate(nums=[1,3,4,8,7,9,3,5,1], k=2)")
    cases.add("candidate(nums=[2,4,2,2,5,2], k=2)")
    cases.add("candidate(nums=[4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], k=14)")
    while len(cases) < 600:
        n = 3 * rng.randint(1, 30)
        nums = [rng.randint(1, 100000) for _ in range(n)]
        k = rng.randint(1, 100000)
        cases.add(f"candidate(nums={nums!r}, k={k})")
    return sorted(cases)
