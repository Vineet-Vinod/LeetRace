import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        starts = [rng.randint(1, 1000) for _ in range(rng.randint(1, 100))]
        ends = [rng.randint(start, 1000) for start in starts]
        query = rng.randint(1, 1000)
        calls.add(
            f"candidate(startTime={starts!r}, endTime={ends!r}, queryTime={query})"
        )
    return sorted(calls)
