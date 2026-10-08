import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: num1..10^8."""
    rng = random.Random(seed)
    values = {1, 9, 555, 100, 10**8}
    while len(values) < 600:
        values.add(rng.randint(1, 10**8))
    return [f"candidate(num={value})" for value in sorted(values)]
