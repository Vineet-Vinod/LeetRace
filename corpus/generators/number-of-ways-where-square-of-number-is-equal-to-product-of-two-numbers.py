def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(nums1=[7, 4], nums2=[5, 2, 8, 9])",
        "candidate(nums1=[1, 1], nums2=[1, 1, 1])",
        "candidate(nums1=[7, 7, 8, 3], nums2=[1, 2, 9, 7])",
        f"candidate(nums1={[1] * 1000!r}, nums2={[1] * 1000!r})",
    }
    while len(cases) < 600:
        mode = rng.randrange(4)
        if mode < 2:
            value = rng.randint(1, 200)
            left_count, right_count = rng.randint(1, 40), rng.randint(1, 40)
            nums1 = [value] * left_count
            nums2 = [value] * right_count
        elif mode == 2:
            value = rng.randint(1, 300)
            factor = rng.randint(1, value)
            if value * value % factor:
                continue
            other = value * value // factor
            if other > 100000:
                continue
            nums1 = [value] * rng.randint(1, 20)
            nums2 = [factor, other] + [
                rng.randint(1, 50) for _ in range(rng.randint(0, 8))
            ]
        else:
            nums1 = [rng.randint(1, 40) for _ in range(rng.randint(1, 30))]
            nums2 = [rng.randint(1, 40) for _ in range(rng.randint(1, 30))]
        assert 1 <= len(nums1) <= 1000 and 1 <= len(nums2) <= 1000
        assert all(1 <= value <= 100000 for value in nums1 + nums2)
        cases.add(f"candidate(nums1={nums1!r}, nums2={nums2!r})")
    return sorted(cases)
