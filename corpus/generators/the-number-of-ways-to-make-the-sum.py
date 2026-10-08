import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    values = set(range(1, 51))
    values.add(100000)
    while len(values) < 600:
        values.add(rng.randint(51, 5000))
    return [f"candidate(n={value})" for value in sorted(values)]
