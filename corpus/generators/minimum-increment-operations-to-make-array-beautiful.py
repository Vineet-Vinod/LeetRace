def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(nums=[2,3,0,0,2],k=4)"}
    while len(cases) < 600:
        n = rng.randint(3, 100)
        nums = [rng.randint(0, 100) for _ in range(n)]
        k = rng.randint(1, 100)
        cases.add(f"candidate(nums={nums!r},k={k})")
    return sorted(cases)
