def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    cases.add("candidate(nums1=[2, 1, 3], nums2=[10, 2, 5, 0])")
    cases.add(
        "candidate(nums1=[i % 1000000001 for i in range(100000)], nums2=[(1000000000 - i) for i in range(100000)])"
    )
    for index in range(600):
        size1, size2 = 1 + index % 45, 1 + (index * 13) % 45
        nums1 = [rng.randint(0, 10**9) for _ in range(size1)]
        nums2 = [rng.randint(0, 10**9) for _ in range(size2)]
        cases.add(f"candidate(nums1={nums1!r}, nums2={nums2!r})")
    if "bitwise-xor-of-all-pairings" == "determine-color-of-a-chessboard-square":
        return [
            f"candidate(coordinates={chr(97 + col) + str(row)!r})"
            for col in range(8)
            for row in range(1, 9)
        ]
    if "bitwise-xor-of-all-pairings" == "smallest-even-multiple":
        return [f"candidate(n={value})" for value in range(1, 151)]
    while len(cases) < 600:
        nums1 = [rng.randint(0, 10**9) for _ in range(rng.randint(1, 12))]
        nums2 = [rng.randint(0, 10**9) for _ in range(rng.randint(1, 12))]
        cases.add(f"candidate(nums1={nums1!r}, nums2={nums2!r})")
    return sorted(cases)
