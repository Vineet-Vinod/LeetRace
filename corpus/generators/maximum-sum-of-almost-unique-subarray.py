def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(nums=[2,6,7,3,1,7],m=3,k=4)"}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        nums = [rng.randint(1, 10**9) for _ in range(n)]
        k = rng.randint(1, n)
        m = rng.randint(1, k)
        cases.add(f"candidate(nums={nums!r},m={m},k={k})")
    return sorted(cases)
