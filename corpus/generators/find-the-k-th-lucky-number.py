import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: k1..10^9."""
    rng = random.Random(seed)
    values = {1, 2, 4, 10, 1000, 10**9}
    while len(values) < 600:
        values.add(rng.randint(1, 10**9))
    return [f"candidate(k={value})" for value in sorted(values)]
