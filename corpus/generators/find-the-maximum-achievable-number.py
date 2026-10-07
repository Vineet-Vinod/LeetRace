import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = {
        f"candidate(num={n}, t={t})" for n, t in ((1, 1), (50, 50), (1, 50), (50, 1))
    }
    while len(calls) < 600:
        calls.add(f"candidate(num={rng.randint(1, 50)}, t={rng.randint(1, 50)})")
    return sorted(calls)
