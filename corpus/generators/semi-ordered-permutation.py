import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        nums = list(range(1, rng.randint(2, 50) + 1))
        rng.shuffle(nums)
        calls.add(f"candidate(nums={nums!r})")
    return sorted(calls)
