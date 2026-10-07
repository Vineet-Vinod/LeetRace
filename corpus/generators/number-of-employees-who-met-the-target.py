import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        hours = [rng.randint(0, 100000) for _ in range(rng.randint(1, 50))]
        target = rng.randint(0, 100000)
        calls.add(f"candidate(hours={hours!r}, target={target})")
    return sorted(calls)
