def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(nums=[0, 1, 0, 0, 1])",
        "candidate(nums=[0, 1, 0])",
        "candidate(nums=[0, 0, 0])",
        f"candidate(nums={[1] * 100000!r})",
        f"candidate(nums={[0] * 99999 + [1]!r})",
    }
    while len(cases) < 600:
        n = rng.randint(1, 100)
        nums = [rng.randrange(2) for _ in range(n)]
        if rng.random() < 0.7:
            nums[rng.randrange(n)] = 1
        assert 1 <= len(nums) <= 100000 and all(x in (0, 1) for x in nums)
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
