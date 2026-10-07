import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: array length 1..10^5; values in 1..n and frequency at most two; generated values satisfy this invariant."""
    rng = random.Random(seed)
    calls = {"candidate(nums=[4, 3, 2, 7, 8, 2, 3, 1])", "candidate(nums=[1])"}
    while len(calls) < 600:
        base_size = rng.randint(1, 400)
        nums = list(range(1, base_size + 1))
        duplicate_values = rng.sample(nums, rng.randint(0, base_size))
        nums.extend(duplicate_values)
        rng.shuffle(nums)
        calls.add(f"candidate(nums={nums!r})")
    return sorted(calls)
