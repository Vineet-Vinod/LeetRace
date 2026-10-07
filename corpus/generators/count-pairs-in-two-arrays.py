import random


def generate(seed: int = 0) -> list[str]:
    """Generate equal-length arrays with values in 1..100000, including max bounds."""
    rng = random.Random(seed)
    boundary_n = 100_000
    calls = [
        "candidate(nums1=[1, 100000], nums2=[100000, 1])",
        f"candidate(nums1={[100_000] * boundary_n!r}, nums2={[1] * boundary_n!r})",
    ]
    seen: set[str] = set(calls)
    index = 0
    while len(calls) < 600:
        n = 1 + index % 40
        nums1 = [rng.randint(1, 100_000) for _ in range(n)]
        nums2 = [rng.randint(1, 100_000) for _ in range(n)]
        assert 1 <= len(nums1) == len(nums2) <= 100_000
        assert all(1 <= value <= 100_000 for value in nums1 + nums2)
        call = f"candidate(nums1={nums1!r}, nums2={nums2!r})"
        index += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
