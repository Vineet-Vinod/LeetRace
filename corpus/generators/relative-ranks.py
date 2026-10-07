import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    calls.add(f"candidate(score={list(range(10000))!r})")
    while len(calls) < 600:
        score = rng.sample(range(0, 1000001), rng.randint(1, 100))
        calls.add(f"candidate(score={score!r})")
    return sorted(calls)
