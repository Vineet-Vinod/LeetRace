import random


def generate(seed: int = 0) -> list[str]:
    """Generate ranges inside [1, 10000], including the upper boundary."""
    rng = random.Random(seed)
    cases = {
        (1, 100),
        (1200, 1230),
        (99, 101),
        (999, 1001),
        (1, 10000),
        (9999, 10000),
        (10000, 10000),
    }
    while len(cases) < 700:
        low = rng.randint(1, 9999)
        high = rng.randint(low, 10000)
        cases.add((low, high))
    return [f"candidate(low={low}, high={high})" for low, high in sorted(cases)]
