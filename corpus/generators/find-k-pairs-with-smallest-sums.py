import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: nondecreasing arrays; lengths1..10^5; k1..10^4 and at most product."""
    rng = random.Random(seed)
    calls = {
        "candidate(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3)",
        "candidate(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2)",
    }
    while len(calls) < 600:
        nums1 = sorted(rng.randint(-100, 100) for _ in range(rng.randint(1, 20)))
        nums2 = sorted(rng.randint(-100, 100) for _ in range(rng.randint(1, 20)))
        k = rng.randint(1, len(nums1) * len(nums2))
        calls.add(f"candidate(nums1={nums1!r}, nums2={nums2!r}, k={k})")
    return sorted(calls)
