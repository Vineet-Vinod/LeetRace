import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: n1..50000; generator uses many n<=1000 plus the 50000 boundary."""
    rng = random.Random(seed)
    values = {1, 2, 9, 10, 13, 100, 1000, 50_000}
    while len(values) < 600:
        values.add(rng.randint(1, 1000))
    return [f"candidate(n={value})" for value in sorted(values)]
