def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    values = {0, 310, -7605, 10**15, -(10**15)}
    while len(values) < 600:
        values.add(rng.randint(-(10**15), 10**15))
    return [f"candidate(num={value})" for value in sorted(values)]
