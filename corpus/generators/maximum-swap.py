def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    values = {0, 2736, 9973, 10**8}
    while len(values) < 600:
        values.add(rng.randint(0, 10**8))
    return [f"candidate(num={value})" for value in sorted(values)]
