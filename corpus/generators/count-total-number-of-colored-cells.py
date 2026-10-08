import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: n 1..100000."""
    rng = random.Random(seed)
    values = {1, 2, 3, 10, 100, 100_000}
    while len(values) < 600:
        values.add(rng.randint(1, 100_000))
    return [f"candidate(n={value})" for value in sorted(values)]
