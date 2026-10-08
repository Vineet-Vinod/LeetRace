def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(nums=[2,-1,1,2,2])",
        "candidate(nums=[-1,2])",
        "candidate(nums=[-2,1,-1,-2,-2])",
    }
    while len(cases) < 600:
        n = rng.randint(1, 60)
        nums = []
        for _ in range(n):
            v = 0
            while v == 0:
                v = rng.randint(-1000, 1000)
            nums.append(v)
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
