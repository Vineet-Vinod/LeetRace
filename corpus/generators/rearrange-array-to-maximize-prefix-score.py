def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(nums=[2,-1,0,1,-3,3,-3])"}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        nums = [rng.randint(-(10**6), 10**6) for _ in range(n)]
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
