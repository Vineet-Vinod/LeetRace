import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    values = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20, 100, 1000, 100000, 1000000}
    for base in (50, 100, 316, 999):
        for delta in (-1, 0, 1):
            values.add(base * (base + 1) // 2 + delta)
            values.add(base * base + delta)
    while len(values) < 600:
        values.add(
            rng.randint(1, 1000) if rng.random() < 0.5 else rng.randint(1, 1000000)
        )
    assert len(values) == 600 and all(1 <= k <= 1000000 for k in values)
    return [f"candidate(k={k})" for k in sorted(values)]
