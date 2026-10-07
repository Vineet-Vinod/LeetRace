def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(nums=[2,1,3,2,1])"}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        nums = [rng.randint(1, 3) for _ in range(n)]
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
