import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    values = {0, 1, 2, 3, 4, 8, 2147395600, 2**31 - 1}
    while len(values) < 600:
        values.add(rng.randint(0, 2**31 - 1))
    return [f"candidate(x={value})" for value in sorted(values)]
