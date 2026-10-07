def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(nums=[2, 6, 4, 8, 10, 9, 15])",
        "candidate(nums=[1, 2, 3, 4])",
        "candidate(nums=[100000, -100000])",
        f"candidate(nums={list(range(10000, 0, -1))!r})",
    }
    while len(cases) < 600:
        n = rng.randint(1, 80)
        nums = [rng.randint(-100000, 100000) for _ in range(n)]
        assert 1 <= len(nums) <= 10000 and all(-100000 <= x <= 100000 for x in nums)
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
