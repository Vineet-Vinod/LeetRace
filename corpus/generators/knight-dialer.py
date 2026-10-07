def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    values = {1, 2, 3, 5000}
    while len(values) < 600:
        values.add(rng.randint(1, 5000))
    return [f"candidate(n={value})" for value in sorted(values)]
