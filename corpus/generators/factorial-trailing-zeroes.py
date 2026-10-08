import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    values = {0, 1, 3, 5, 24, 25, 26, 100, 10_000}
    while len(values) < 600:
        values.add(rng.randint(0, 10_000))
    assert all(0 <= n <= 10_000 for n in values)
    return [f"candidate(n={n})" for n in sorted(values)]
