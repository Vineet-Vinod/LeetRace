import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: num 0..10^9."""
    rng = random.Random(seed)
    values = {0, 1, 2, 23, 107, 10**9}
    while len(values) < 600:
        values.add(rng.randint(0, 10**9))
    return [f"candidate(num={value})" for value in sorted(values)]
