def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(300):
        nums = []
        target = rng.randint(2, 100)
        while len(nums) < 2 or len(nums) < target and len(nums) <= 97:
            group = rng.randrange(3)
            group_size = 2 if group == 0 else 3
            if len(nums) + group_size > 100:
                group = 0
                group_size = 2
            value = rng.randint(1, 999998)
            if group == 0:
                nums.extend([value, value])
            elif group == 1:
                nums.extend([value, value, value])
            else:
                nums.extend([value, value + 1, value + 2])
        cases.add(f"candidate(nums={nums!r})")
    for _ in range(300):
        nums = [rng.randint(1, 1000000) for _ in range(rng.randint(2, 100))]
        cases.add(f"candidate(nums={nums!r})")
    cases.update(
        {
            "candidate(nums=[4, 4, 4, 5, 6])",
            "candidate(nums=[1, 1, 1, 2])",
            "candidate(nums=[1, 2])",
            "candidate(nums=[1, 2, 3])",
            "candidate(nums=[1, 1, 2, 2])",
        }
    )
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(nums={[1] * 100000!r})"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
