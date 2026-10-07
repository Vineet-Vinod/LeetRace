import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    values = {0, 1, 24, 25, 50, 100, 500, 4800, 10**9}
    while len(values) < 600:
        values.add(rng.randint(0, 10**9))
    assert all(0 <= value <= 10**9 for value in values)
    return [f"candidate(n={value})" for value in sorted(values)]
