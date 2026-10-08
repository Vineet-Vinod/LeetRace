import random


def generate(seed: int = 0) -> list[str]:
    """Mix feasible swap patterns, impossible inputs, and maximum-size boundaries."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    index = 0

    while len(calls) < 300:
        size = 1 + index % 40
        low, high = 500_000_000, 1_000_000_000
        nums1: list[int] = []
        nums2: list[int] = []
        for _ in range(size - 1):
            if rng.randrange(2):
                nums1.append(rng.randint(1, low))
                nums2.append(rng.randint(1, high))
            else:
                nums1.append(rng.randint(low + 1, high))
                nums2.append(rng.randint(1, low))
        nums1.append(low)
        nums2.append(high)
        assert len(nums1) == len(nums2) == size
        assert all(1 <= value <= 10**9 for value in nums1 + nums2)
        call = f"candidate(nums1={nums1!r}, nums2={nums2!r})"
        index += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)

    size = 1000
    nums1 = [500_000_000 if i % 2 == 0 else 1_000_000_000 for i in range(size)]
    nums2 = [1_000_000_000 if i % 2 == 0 else 500_000_000 for i in range(size)]
    calls.append(f"candidate(nums1={nums1!r}, nums2={nums2!r})")
    seen.add(calls[-1])

    while len(calls) < 600:
        size = 1 + index % 40
        nums1 = [rng.randint(1, 1000) for _ in range(size)]
        nums2 = [rng.randint(1, 1000) for _ in range(size)]
        call = f"candidate(nums1={nums1!r}, nums2={nums2!r})"
        index += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
