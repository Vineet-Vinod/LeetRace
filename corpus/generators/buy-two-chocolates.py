import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        prices = [rng.randint(1, 100) for _ in range(rng.randint(2, 50))]
        money = rng.randint(1, 100)
        calls.add(f"candidate(prices={prices!r}, money={money})")
    return sorted(calls)
