import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = {f"candidate(n={n})" for n in range(1, 31)}
    while len(calls) < 600:
        calls.add(f"candidate(n={rng.randint(1, 1000)})")
    return sorted(calls)
