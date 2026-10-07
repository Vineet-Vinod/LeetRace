import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: nums length2..1000, values1..10^7, k1..1000; generated input within bounds."""
    rng = random.Random(seed)
    calls = {
        "candidate(nums=[1, 2, 3, 4, 5], k=2)",
        "candidate(nums=[1, 4, 2, 3, 1, 4], k=3)",
    }
    while len(calls) < 600:
        size = rng.randint(2, 80)
        nums = [rng.randint(1, 10**7) for _ in range(size)]
        k = rng.randint(1, 50)
        calls.add(f"candidate(nums={nums!r}, k={k})")
    return sorted(calls)
