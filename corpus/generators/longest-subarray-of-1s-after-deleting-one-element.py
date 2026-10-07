import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: binary nums length1..10^5; includes length100000 all-one boundary."""
    rng = random.Random(seed)
    calls = {
        "candidate(nums=[1, 1, 0, 1])",
        "candidate(nums=[1, 1, 1])",
        f"candidate(nums={[1] * 100000!r})",
    }
    while len(calls) < 600:
        nums = [rng.randint(0, 1) for _ in range(rng.randint(1, 500))]
        calls.add(f"candidate(nums={nums!r})")
    return sorted(calls)
