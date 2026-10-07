def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(nums=[1, 2, 3, 6])",
        "candidate(nums=[2, 3, 4, 6])",
        "candidate(nums=[1, 2, 4, 8])",
        "candidate(nums=[1, 2, 3, 4, 6, 8, 12])",
        f"candidate(nums={list(range(1, 1001))!r})",
    }
    while len(cases) < 350:
        while True:
            first_factor = rng.randint(2, 60)
            second_factor = rng.randint(2, 60)
            left_factor = rng.randint(2, 60)
            right_factor = rng.randint(2, 60)
            nums = {
                first_factor * left_factor,
                first_factor * right_factor,
                second_factor * left_factor,
                second_factor * right_factor,
            }
            if len(nums) == 4 and max(nums) <= 10000:
                break
        for _ in range(rng.randint(0, 20)):
            value = rng.randint(1, 10000)
            if value not in nums:
                nums.add(value)
        values = sorted(nums)
        assert len(values) == len(set(values)) and all(
            1 <= value <= 10000 for value in values
        )
        cases.add(f"candidate(nums={values!r})")

    while len(cases) < 600:
        nums = rng.sample(range(1, 10001), rng.randint(1, 50))
        assert len(nums) == len(set(nums))
        cases.add(f"candidate(nums={nums!r})")
    assert len(cases) == 600
    return sorted(cases)
