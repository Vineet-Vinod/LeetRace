def generate(seed: int = 0) -> list[str]:
    # Seeded random inputs stay within stated bounds; structural preconditions are enforced below.
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(nums=[-1,0,1,2,-1,-4])",
        "candidate(nums=[0,0,0])",
        "candidate(nums=[-100000,0,100000])",
    }
    while len(cases) < 600:
        n = rng.randint(3, 24)
        nums = [rng.randint(-100000, 100000) for _ in range(n)]
        if rng.random() < 0.4:
            x = rng.randint(-100, 100)
            nums.extend([x, x, -2 * x])
        nums = nums[:3000]
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
