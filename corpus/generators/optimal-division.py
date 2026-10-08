def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(nums=[2,3,4])"}
    while len(cases) < 600:
        n = rng.randint(1, 10)
        nums = [rng.randint(2, 1000) for _ in range(n)]
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
