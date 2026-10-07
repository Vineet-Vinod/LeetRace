import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: sorted nondecreasing nums length1..10^5, positive values<=10^9."""
    rng = random.Random(seed)
    calls = {
        "candidate(nums=[1, 2, 3, 4])",
        "candidate(nums=[1, 1, 2, 2, 3, 3])",
        "candidate(nums=[1000000000, 1000000000])",
    }
    while len(calls) < 600:
        nums = sorted(rng.randint(1, 1000) for _ in range(rng.randint(1, 1000)))
        calls.add(f"candidate(nums={nums!r})")
    return sorted(calls)
