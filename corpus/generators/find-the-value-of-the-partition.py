import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: positive nums length2..10^5, values1..10^9."""
    rng = random.Random(seed)
    calls = {"candidate(nums=[1, 3, 2, 4])", "candidate(nums=[100, 1, 10])"}
    while len(calls) < 600:
        nums = [rng.randint(1, 10**9) for _ in range(rng.randint(2, 80))]
        calls.add(f"candidate(nums={nums!r})")
    return sorted(calls)
