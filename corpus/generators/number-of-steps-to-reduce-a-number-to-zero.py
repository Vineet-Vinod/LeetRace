import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: num in [0,10^6]."""
    rng = random.Random(seed)
    values = set(range(500))
    while len(values) < 600:
        values.add(rng.randint(0, 10**6))
    values.add(10**6)
    return [f"candidate(num={n})" for n in values]
