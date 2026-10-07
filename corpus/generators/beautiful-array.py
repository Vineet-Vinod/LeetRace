import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: n is 1..1000 as stated; 600 unique seeded values cover small, boundary, and broad random sizes.."""
    rng = random.Random(seed)
    values = {1, 2, 3, 4, 5, 999, 1000}
    while len(values) < 600:
        values.add(rng.randint(1, 1000))
    return [f"candidate(n={value})" for value in sorted(values)]
