def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(nums1=[55, 30, 5, 4, 2], nums2=[100, 20, 10, 10, 5])"])
    for index in range(600):
        size1 = 1 + index % 100
        size2 = 1 + (index * 7) % 100
        if index == 0:
            size1, size2 = 100000, 100000
        nums1 = sorted((rng.randint(1, 100000) for _ in range(size1)), reverse=True)
        nums2 = sorted((rng.randint(1, 100000) for _ in range(size2)), reverse=True)
        cases.add(f"candidate(nums1={nums1!r}, nums2={nums2!r})")
    return sorted(cases)
