import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: n 0..10^9."""
    rng = random.Random(seed)
    values = {0, 1, 2, 3, 4, 8, 9, 10, 10**9}
    while len(values) < 600:
        values.add(rng.randint(0, 10**9))
    return [f"candidate(n={value})" for value in sorted(values)]
