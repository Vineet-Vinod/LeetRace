import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    values = list(range(1, 1001))
    rng.shuffle(values)
    return [f"candidate(n={n})" for n in values[:600]]
