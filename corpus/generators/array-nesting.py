def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for size in range(1, 71):
        nums = list(range(size))
        rng.shuffle(nums)
        cases.add(f"candidate(nums={nums!r})")

    nums = list(range(100000))
    rng.shuffle(nums)
    assert len(nums) == 100000 and sorted(nums) == list(range(100000))
    boundary = f"candidate(nums={nums!r})"
    cases.add(boundary)
    while len(cases) < 600:
        size = rng.randint(1, 1000)
        nums = list(range(size))
        rng.shuffle(nums)
        assert len(nums) == size and sorted(nums) == list(range(size))
        cases.add(f"candidate(nums={nums!r})")
    if len(cases) > 600:
        cases.remove(max(cases - {boundary}))
    assert len(cases) == 600
    return sorted(cases)
