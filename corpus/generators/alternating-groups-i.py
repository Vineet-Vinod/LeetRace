import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        size = rng.randint(3, 100)
        colors = [rng.randrange(2) for _ in range(size)]
        calls.add(f"candidate(colors={colors!r})")
    return sorted(calls)
