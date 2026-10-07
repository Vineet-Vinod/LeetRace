import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        nums = [
            rng.choice([value for value in range(-1000, 1001) if value])
            for _ in range(rng.randint(1, 1000))
        ]
        calls.add(f"candidate(nums={nums!r})")
    return sorted(calls)
