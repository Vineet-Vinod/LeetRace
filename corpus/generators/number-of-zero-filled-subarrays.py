def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        nums = [rng.randint(-(10**9), 10**9) for _ in range(rng.randint(1, 100))]
        if rng.random() < 0.8:
            start = rng.randrange(len(nums))
            end = min(len(nums), start + rng.randint(1, 20))
            nums[start:end] = [0] * (end - start)
        cases.add(f"candidate(nums={nums!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(nums={[0] * 100000!r})"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
