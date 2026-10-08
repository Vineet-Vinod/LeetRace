def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(nums=[1, 2, 3])",
        "candidate(nums=[2, 4, 6, 4])",
        "candidate(nums=[3, 2, 1])",
        f"candidate(nums={list(range(1, 100001))!r})",
    }
    while len(cases) < 600:
        n = rng.randint(3, 100)
        mode = rng.randrange(3)
        if mode == 0:
            nums = sorted(rng.randint(1, 100000) for _ in range(n))
        elif mode == 1:
            nums = list(reversed(sorted(rng.randint(1, 100000) for _ in range(n))))
        else:
            nums = [rng.randint(1, 100000) for _ in range(n)]
        assert 3 <= len(nums) <= 100000 and all(1 <= x <= 100000 for x in nums)
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
