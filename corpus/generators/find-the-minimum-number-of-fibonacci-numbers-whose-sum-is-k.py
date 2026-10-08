import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    values = {1, 2, 7, 10, 19, 10**9}
    while len(values) < 600:
        values.add(rng.randint(1, 10**9))
    assert all(1 <= value <= 10**9 for value in values)
    return [f"candidate(k={value})" for value in sorted(values)]
