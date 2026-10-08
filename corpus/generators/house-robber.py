def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(nums=[1, 2, 3, 1])",
        "candidate(nums=[2, 7, 9, 3, 1])",
        f"candidate(nums={[0] * 100!r})",
        f"candidate(nums={[400] * 100!r})",
        f"candidate(nums={[400 if index % 2 == 0 else 0 for index in range(100)]!r})",
        f"candidate(nums={[0 if index % 2 == 0 else 400 for index in range(100)]!r})",
        "candidate(nums=[0])",
        "candidate(nums=[400])",
    }
    while len(cases) < 600:
        nums = [rng.randint(0, 400) for _ in range(rng.randint(1, 100))]
        assert 1 <= len(nums) <= 100 and all(0 <= value <= 400 for value in nums)
        cases.add(f"candidate(nums={nums!r})")
    assert len(cases) == 600
    return sorted(cases)
