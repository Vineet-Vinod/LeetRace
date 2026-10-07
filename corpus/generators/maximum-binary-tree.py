import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: nums length1..1000; unique values0..1000."""
    rng = random.Random(seed)
    calls = {"candidate(nums=[3, 2, 1, 6, 0, 5])", "candidate(nums=[3, 2, 1])"}
    while len(calls) < 600:
        nums = rng.sample(range(1001), rng.randint(1, 80))
        calls.add(f"candidate(nums={nums!r})")
    return sorted(calls)
