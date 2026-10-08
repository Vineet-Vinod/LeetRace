import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: distinct positive nums length1..1000, values<=2*10^9."""
    rng = random.Random(seed)
    calls = {
        "candidate(nums=[1, 2, 3])",
        "candidate(nums=[1, 2, 4, 8])",
        "candidate(nums=[1, 2, 4, 8, 16, 32, 64])",
    }
    while len(calls) < 600:
        nums = rng.sample(range(1, 2_000_000_001), rng.randint(1, 60))
        calls.add(f"candidate(nums={nums!r})")
    return sorted(calls)
