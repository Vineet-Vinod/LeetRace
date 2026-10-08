def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        size = rng.randint(1, 100)
        start = rng.randint(-5000, 5000 - size + 1)
        nums = list(range(start, start + size))
        rotation = rng.randrange(size)
        nums = nums[rotation:] + nums[:rotation]
        assert len(nums) == len(set(nums))
        cases.add(f"candidate(nums={nums!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(nums={list(range(2500, 5000)) + list(range(2500))!r})"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
