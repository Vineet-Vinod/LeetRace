import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: positive nums length1..10^5, values1..10^6; includes 100000-element boundary."""
    rng = random.Random(seed)
    calls = {
        "candidate(nums=[4, 3, 2, 1, 2, 3, 1])",
        "candidate(nums=[1, 2, 3, 4])",
        f"candidate(nums={[1] * 100000!r})",
    }
    while len(calls) < 600:
        nums = [rng.randint(1, 10**6) for _ in range(rng.randint(1, 300))]
        calls.add(f"candidate(nums={nums!r})")
    return sorted(calls)
