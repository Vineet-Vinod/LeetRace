import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = {
        f"candidate(red={r}, blue={b})"
        for r, b in ((1, 1), (100, 100), (1, 100), (100, 1))
    }
    while len(calls) < 600:
        calls.add(f"candidate(red={rng.randint(1, 100)}, blue={rng.randint(1, 100)})")
    return sorted(calls)
