import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    values = {1, 4, 9, 40, 90, 400, 900, 58, 1994, 3749, 3999}
    while len(values) < 600:
        values.add(rng.randint(1, 3999))
    assert all(1 <= value <= 3999 for value in values)
    return [f"candidate(num={value})" for value in sorted(values)]
