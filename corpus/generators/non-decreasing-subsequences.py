def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(nums=[4,6,7,7])"}
    while len(cases) < 600:
        n = rng.randint(1, 15)
        nums = [rng.randint(-100, 100) for _ in range(n)]
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
