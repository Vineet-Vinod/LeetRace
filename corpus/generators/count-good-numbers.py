import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    values = {1, 2, 3, 4, 5, 10, 99, 10**15}
    while len(values) < 600:
        values.add(rng.randint(1, 10**15))
    return [f"candidate(n={n})" for n in sorted(values)]
