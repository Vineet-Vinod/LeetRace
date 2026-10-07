import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: equal arrays length1..10^5; values0..10^5; 1<=k<=n."""
    rng = random.Random(seed)
    calls = {
        "candidate(nums1=[1, 3, 3, 2], nums2=[2, 1, 3, 4], k=3)",
        "candidate(nums1=[4, 2, 3, 1, 1], nums2=[7, 5, 10, 9, 6], k=1)",
    }
    while len(calls) < 600:
        size = rng.randint(1, 100)
        nums1 = [rng.randint(0, 100_000) for _ in range(size)]
        nums2 = [rng.randint(0, 100_000) for _ in range(size)]
        calls.add(
            f"candidate(nums1={nums1!r}, nums2={nums2!r}, k={rng.randint(1, size)})"
        )
    return sorted(calls)
