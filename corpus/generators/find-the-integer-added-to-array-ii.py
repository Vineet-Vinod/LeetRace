def _generate_base(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    for _ in range(600):
        size = rng.randint(3, 50)
        nums1 = [rng.randint(0, 1000) for _ in range(size)]
        removed = set(rng.sample(range(size), 2))
        shift_low = max(
            -value for index, value in enumerate(nums1) if index not in removed
        )
        shift_high = min(
            1000 - value for index, value in enumerate(nums1) if index not in removed
        )
        shift = rng.randint(shift_low, shift_high)
        nums2 = [
            value + shift for index, value in enumerate(nums1) if index not in removed
        ]
        rng.shuffle(nums1)
        rng.shuffle(nums2)
        assert len(nums2) == len(nums1) - 2 and all(
            0 <= value <= 1000 for value in nums2
        )
        cases.add(f"candidate(nums1={nums1!r}, nums2={nums2!r})")
    assert len(cases) >= 500
    return sorted(cases)[:600]


def generate(seed: int = 0) -> list[str]:
    calls = _generate_base(seed)
    boundary = f"candidate(nums1={list(range(200))!r}, nums2={list(range(198))!r})"
    if boundary not in calls:
        calls[-1] = boundary
    assert 500 <= len(calls) <= 999
    return calls
