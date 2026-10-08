import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: nums length1..10^5, values0..10^9; includes length100000 boundary."""
    rng = random.Random(seed)
    calls = {
        "candidate(nums=[1, 3, 5, 2, 1, 3, 1])",
        "candidate(nums=[1, 2, 3, 4])",
        f"candidate(nums={[rng.randrange(10**9 + 1) for _ in range(100000)]!r})",
    }
    while len(calls) < 600:
        nums = [rng.randint(0, 10**9) for _ in range(rng.randint(1, 100))]
        calls.add(f"candidate(nums={nums!r})")
    return sorted(calls)
