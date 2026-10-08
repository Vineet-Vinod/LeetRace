import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    values = {0, 1, -1, 16, -16, 2**31 - 1, -(2**31)}
    while len(values) < 600:
        values.add(rng.randint(-(2**31), 2**31 - 1))
    return [f"candidate(num={value})" for value in sorted(values)]
