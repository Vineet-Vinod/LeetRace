import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        intervals = []
        for _ in range(rng.randint(1, 100)):
            start = rng.randint(1, 100)
            end = rng.randint(start, 100)
            intervals.append([start, end])
        calls.add(f"candidate(nums={intervals!r})")
    return sorted(calls)
