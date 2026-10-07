import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: nums length2..1000; values0..500; generator includes length1000 valid boundary."""
    rng = random.Random(seed)
    calls = {
        "candidate(nums=[3, 6, 9, 12])",
        "candidate(nums=[9, 4, 7, 2, 10])",
        f"candidate(nums={[i % 501 for i in range(1000)]!r})",
    }
    while len(calls) < 600:
        nums = [rng.randint(0, 500) for _ in range(rng.randint(2, 60))]
        calls.add(f"candidate(nums={nums!r})")
    return sorted(calls)
