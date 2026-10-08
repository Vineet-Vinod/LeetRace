def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(nums1=[0],nums2=[1])",
        "candidate(nums1=[1000000],nums2=[1000000])",
        f"candidate(nums1={[0] * 100000!r},nums2={[1] * 100000!r})",
        f"candidate(nums1={[1] * 100000!r},nums2={[1] * 100000!r})",
    }
    while len(cases) < 600:
        if rng.random() < 0.5:
            nums1 = [rng.randint(0, 1000) for _ in range(rng.randint(1, 30))]
            nums2 = [rng.randint(0, 1000) for _ in range(rng.randint(1, 30))]
            if not any(value == 0 for value in nums1):
                nums1[rng.randrange(len(nums1))] = 0
            if not any(value == 0 for value in nums2):
                nums2[rng.randrange(len(nums2))] = 0
        else:
            nums1 = [rng.randint(1, 1000) for _ in range(rng.randint(1, 30))]
            nums2 = [rng.randint(1, 1000) for _ in range(rng.randint(1, 30))]
            if sum(nums1) == sum(nums2):
                nums2[-1] = (nums2[-1] % 1000) + 1
        assert 1 <= len(nums1) <= 100000 and 1 <= len(nums2) <= 100000
        assert all(0 <= value <= 10**6 for value in nums1 + nums2)
        cases.add(f"candidate(nums1={nums1!r},nums2={nums2!r})")
    return sorted(cases)
