def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(nums=[8, 4, 2, 30, 15])",
        "candidate(nums=[1, 2, 3, 4, 5])",
        "candidate(nums=[3, 16, 8, 4, 2])",
        "candidate(nums=[256, 3])",
        f"candidate(nums={[1 << i for i in range(8)] * 12 + [256] * 4!r})",
    }
    one_bit = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    while len(cases) < 600:
        n = rng.randint(1, 100)
        if rng.random() < 0.55:
            nums = [rng.choice(one_bit) for _ in range(n)]
            rng.shuffle(nums)
        elif rng.random() < 0.5 and n >= 2:
            high = rng.choice([8, 16, 32, 64, 128, 256])
            low = rng.choice([3, 5, 6, 7, 9, 10, 12])
            nums = [high, low] + [rng.randint(1, 256) for _ in range(n - 2)]
        else:
            nums = [rng.randint(1, 256) for _ in range(n)]
        assert 1 <= len(nums) <= 100 and all(1 <= value <= 256 for value in nums)
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
