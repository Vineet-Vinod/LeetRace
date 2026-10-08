def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    values = {1, 13, 10**9, 10**15}
    while len(values) < 600:
        values.add(rng.randint(1, 10**15))
    return [f"candidate(neededApples={value})" for value in sorted(values)]
