import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        nums = [rng.randint(1, 100) for _ in range(rng.randint(1, 100))]
        k = rng.randint(1, 100)
        calls.add(f"candidate(nums={nums!r}, k={k})")
    return sorted(calls)
