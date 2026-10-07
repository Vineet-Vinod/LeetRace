import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: nums length1..10^5; positive values<=10^9; includes length100000 boundary."""
    rng = random.Random(seed)
    calls = {
        "candidate(nums=[1, 3, 8, 48, 10])",
        "candidate(nums=[3, 1, 5, 11, 13])",
        f"candidate(nums={[1 << (i % 30) for i in range(100000)]!r})",
    }
    while len(calls) < 600:
        nums = [rng.randint(1, 10**9) for _ in range(rng.randint(1, 500))]
        calls.add(f"candidate(nums={nums!r})")
    return sorted(calls)
