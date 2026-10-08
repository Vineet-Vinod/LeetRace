def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(nums=[1, -10, 7, 13, 6, 8], value=5)",
        "candidate(nums=[1, 2, 3], value=1)",
        "candidate(nums=[-1, -2, -3], value=1)",
        f"candidate(nums={list(range(100000))!r}, value=1)",
        f"candidate(nums={[0] * 100000!r}, value=100000)",
        f"candidate(nums={list(range(-50000, 50000))!r}, value=7)",
    }
    while len(cases) < 600:
        value = rng.randint(1, 100)
        nums = [rng.randint(-1000, 1000) for _ in range(rng.randint(1, 100))]
        if rng.random() < 0.7:
            residue = rng.randrange(value)
            nums.extend(
                residue + value * rng.randint(-10, 10)
                for _ in range(rng.randint(1, 30))
            )
        assert 1 <= len(nums) <= 100000 and 1 <= value <= 100000
        assert all(-(10**9) <= number <= 10**9 for number in nums)
        cases.add(f"candidate(nums={nums!r}, value={value})")
    assert len(cases) == 600
    return sorted(cases)
