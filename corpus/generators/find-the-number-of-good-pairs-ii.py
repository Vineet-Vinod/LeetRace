import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: arrays lengths1..10^5; values1..10^6; k1..10^3."""
    rng = random.Random(seed)
    calls = {
        "candidate(nums1=[1, 3, 4], nums2=[1, 3, 4], k=1)",
        "candidate(nums1=[1, 2, 4, 12], nums2=[2, 4], k=3)",
    }
    while len(calls) < 600:
        nums1 = [rng.randint(1, 2000) for _ in range(rng.randint(1, 40))]
        nums2 = [rng.randint(1, 2000) for _ in range(rng.randint(1, 40))]
        k = rng.randint(1, 50)
        calls.add(f"candidate(nums1={nums1!r}, nums2={nums2!r}, k={k})")
    return sorted(calls)
