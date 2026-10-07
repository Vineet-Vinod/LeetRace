import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    values = {1, 2, 3, 12, 31, 32, 33, 100_000}
    while len(values) < 600:
        values.add(rng.randint(1, 100_000))
    assert all(1 <= n <= 100_000 for n in values)
    return [f"candidate(n={n})" for n in sorted(values)]
