def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    values = {1, 8, 123, 999, 10**9}
    while len(values) < 600:
        values.add(rng.randint(1, 10**9))
    return [f"candidate(num={value})" for value in sorted(values)]
