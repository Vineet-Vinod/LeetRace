def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(nums=[1],k=0)",
        "candidate(nums=[0,100000,0],k=1)",
        "candidate(nums=[100000],k=100000)",
        f"candidate(nums={list(range(100000))!r},k=50000)",
    }
    while len(cases) < 600:
        n = rng.randint(1, 100)
        nums = [rng.randint(0, 100000) for _ in range(n)]
        k = rng.choice([0, 1, n // 2, n, 100000, rng.randint(0, 100)])
        assert 1 <= len(nums) <= 100000
        assert all(0 <= value <= 100000 for value in nums)
        assert 0 <= k <= 100000
        cases.add(f"candidate(nums={nums!r},k={k})")
    return sorted(cases)
