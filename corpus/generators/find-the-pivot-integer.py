import random


def generate(seed: int = 0) -> list[str]:
    """Include all pivots in [1, 1000] and varied legal non-pivots."""
    rng = random.Random(seed)
    pivots = {1, 8, 49, 288}
    values = {1, 4, 8, 49, 288, 1000}
    while len(values) < 600:
        values.add(rng.randint(1, 1000))
    assert len(values) == 600
    assert all(1 <= value <= 1000 for value in values)
    assert pivots <= values
    return [f"candidate(n={value})" for value in sorted(values)]
