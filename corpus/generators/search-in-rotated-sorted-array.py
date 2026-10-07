def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    max_present = list(range(-2500, 2500))
    max_absent = list(range(-10000, -5000))
    cases = {
        f"candidate(nums={max_present!r},target=0)",
        f"candidate(nums={max_absent!r},target=10000)",
        "candidate(nums=[10000],target=10000)",
    }
    while len(cases) < 600:
        n = rng.randint(1, 100)
        ordered = sorted(rng.sample(range(-10000, 10001), n))
        pivot = rng.randrange(n)
        nums = ordered[pivot:] + ordered[:pivot]
        if rng.random() < 0.5:
            target = rng.choice(nums)
        else:
            existing = set(nums)
            target = rng.randint(-10000, 10000)
            while target in existing:
                target = rng.randint(-10000, 10000)
        assert 1 <= len(nums) <= 5000 and len(set(nums)) == len(nums)
        assert all(-10000 <= value <= 10000 for value in nums)
        assert -10000 <= target <= 10000
        cases.add(f"candidate(nums={nums!r},target={target})")
    return sorted(cases)
