import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: nums length1..100; values0..1000."""
    rng = random.Random(seed)
    calls = {
        "candidate(nums=[2, 3, 2])",
        "candidate(nums=[1, 2, 3, 1])",
        "candidate(nums=[0])",
    }
    while len(calls) < 600:
        nums = [rng.randint(0, 1000) for _ in range(rng.randint(1, 100))]
        calls.add(f"candidate(nums={nums!r})")
    return sorted(calls)
