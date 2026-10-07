import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    values = {1, 2, 3, 4, 2**31 - 1}
    while len(values) < 600:
        values.add(rng.randint(1, 2**31 - 1))
    return [f"candidate(n={n})" for n in sorted(values)]
