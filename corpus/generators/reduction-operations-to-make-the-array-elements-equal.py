def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(nums=[5, 1, 3])",
        "candidate(nums=[1, 1, 1])",
        "candidate(nums=[1, 1, 2, 2, 3])",
        f"candidate(nums={[1] * 50000!r})",
        f"candidate(nums={[50000] * 50000!r})",
        f"candidate(nums={[1, 50000] * 25000!r})",
        f"candidate(nums={[1, 2, 2, 50000] * 12500!r})",
        f"candidate(nums={list(range(1, 50001))!r})",
    }
    while len(cases) < 600:
        nums = [rng.randint(1, 50000) for _ in range(rng.randint(1, 100))]
        assert 1 <= len(nums) <= 50000 and all(1 <= value <= 50000 for value in nums)
        cases.add(f"candidate(nums={nums!r})")
    assert len(cases) == 600
    return sorted(cases)
