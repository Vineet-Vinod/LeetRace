import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: n 1..10^9."""
    rng = random.Random(seed)
    values = {1, 2, 9, 10, 403, 999, 1000, 10**9}
    while len(values) < 600:
        values.add(rng.randint(1, 10**9))
    return [f"candidate(n={value})" for value in sorted(values)]
