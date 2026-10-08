import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = {
        "(lambda nums: (lambda k: (k, nums[:k]))(candidate(nums)))([1] * 30000)"
    }
    while len(calls) < 600:
        nums = sorted(rng.randint(-10000, 10000) for _ in range(rng.randint(1, 300)))
        calls.add(
            f"(lambda nums: (lambda k: (k, nums[:k]))(candidate(nums)))({nums!r})"
        )
    return sorted(calls)
