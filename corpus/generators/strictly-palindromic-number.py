def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    values = set(range(4, 104))
    values.update([100000, 99999, 50000])
    while len(values) < 600:
        values.add(rng.randint(4, 100000))
    assert len(values) == 600 and all(4 <= value <= 100000 for value in values)
    return [f"candidate(n={value})" for value in sorted(values)]
