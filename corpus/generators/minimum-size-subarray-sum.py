def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(target=7, nums=[2, 3, 1, 2, 4, 3])",
        "candidate(target=4, nums=[1, 4, 4])",
        "candidate(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1])",
        "candidate(target=3, nums=[1, 1, 1])",
        f"candidate(target=50000, nums={[1] * 100000!r})",
        f"candidate(target=1000000000, nums={[10000] * 100000!r})",
        f"candidate(target=1000000000, nums={[1] * 100000!r})",
        f"candidate(target=1, nums={[10000] * 100000!r})",
    }
    while len(cases) < 600:
        nums = [rng.randint(1, 10000) for _ in range(rng.randint(1, 100))]
        total = sum(nums)
        target = rng.randint(1, min(10**9, total + 1000))
        assert 1 <= len(nums) <= 100000 and all(1 <= value <= 10000 for value in nums)
        assert 1 <= target <= 10**9
        cases.add(f"candidate(target={target}, nums={nums!r})")
    assert len(cases) == 600
    return sorted(cases)
