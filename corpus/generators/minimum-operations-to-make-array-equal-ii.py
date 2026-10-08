def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(nums1=[4, 3, 1, 4], nums2=[1, 3, 7, 1], k=3)",
        "candidate(nums1=[3, 8, 5, 2], nums2=[2, 4, 1, 6], k=1)",
        "candidate(nums1=[1, 2], nums2=[1, 2], k=0)",
        "candidate(nums1=[1, 2], nums2=[2, 1], k=0)",
        f"candidate(nums1={[0] * 100000!r}, nums2={[0] * 100000!r}, k=0)",
    }
    while len(cases) < 600:
        n = rng.randint(2, 50)
        k = rng.randint(1, 100000)
        nums2 = [500_000_000] * n
        units = [0] * n
        mode = rng.randrange(4)
        if mode == 0:
            for _ in range(rng.randint(1, 20)):
                i, j = rng.sample(range(n), 2)
                amount = rng.randint(1, 20)
                units[i] += amount
                units[j] -= amount
            nums1 = [base + k * amount for base, amount in zip(nums2, units)]
        elif mode == 1:
            nums1 = nums2[:]
            k = 0
        elif mode == 2:
            nums1 = nums2[:]
            nums1[0] += 1
        else:
            units[0] = rng.randint(1, 20)
            nums1 = [base + k * amount for base, amount in zip(nums2, units)]
        assert len(nums1) == len(nums2) == n and 2 <= n <= 100000
        assert all(0 <= value <= 10**9 for value in nums1 + nums2) and 0 <= k <= 100000
        cases.add(f"candidate(nums1={nums1!r}, nums2={nums2!r}, k={k})")
    return sorted(cases)
