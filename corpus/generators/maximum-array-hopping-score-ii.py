def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(nums=[1,5,8])"}
    while len(cases) < 600:
        n = rng.randint(2, 100)
        nums = [rng.randint(1, 10**5) for _ in range(n)]
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
