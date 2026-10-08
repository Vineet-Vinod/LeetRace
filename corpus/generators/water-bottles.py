import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = {
        f"candidate(numBottles={b}, numExchange={e})"
        for b, e in ((1, 2), (100, 2), (100, 100), (9, 3), (15, 4))
    }
    while len(calls) < 600:
        calls.add(
            f"candidate(numBottles={rng.randint(1, 100)}, numExchange={rng.randint(2, 100)})"
        )
    return sorted(calls)
