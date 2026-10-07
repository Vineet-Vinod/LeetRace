def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(nums=[2,6,3,4])"}
    while len(cases) < 600:
        n = rng.randint(2, 50)
        nums = [rng.randint(1, 100) for _ in range(n)]
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
