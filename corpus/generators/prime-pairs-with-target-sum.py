def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    values = {1, 2, 10, 100, 10**6}
    while len(values) < 600:
        values.add(rng.randint(1, 10000))
    return [f"candidate(n={value})" for value in sorted(values)]
