def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(nums=[1,0,2,0,1,2])"}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        nums = [rng.randint(0, 10**6) for _ in range(n)]
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
