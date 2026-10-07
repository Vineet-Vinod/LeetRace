import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: nums length1..10^5; entries -10^5..10^5."""
    rng = random.Random(seed)
    calls = {
        "candidate(nums=[3, -1, 1, 2])",
        "candidate(nums=[2, 2, 2, 2, 2])",
        "candidate(nums=[1])",
    }
    while len(calls) < 600:
        nums = [rng.randint(-100_000, 100_000) for _ in range(rng.randint(1, 200))]
        calls.add(f"candidate(nums={nums!r})")
    return sorted(calls)
