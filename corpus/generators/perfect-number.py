import random


def generate(seed: int = 0) -> list[str]:
    """Include every perfect number in [1, 10^8], plus varied in-bound negatives."""
    rng = random.Random(seed)
    perfect = {6, 28, 496, 8128, 33550336}
    values = {1, 2, 7, *perfect, 100_000_000}
    while len(values) < 600:
        values.add(rng.randint(1, 100_000_000))
    assert len(values) == 600
    assert all(1 <= value <= 100_000_000 for value in values)
    assert perfect <= values
    return [f"candidate(num={value})" for value in sorted(values)]
