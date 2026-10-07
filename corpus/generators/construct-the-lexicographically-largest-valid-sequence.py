import random

DOMAIN_SIZE = 20


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    values = list(range(1, 21))
    rng.shuffle(values)
    return [f"candidate(n={n})" for n in values]
