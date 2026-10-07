import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: equal nonempty arrays length up to20000; customer counts0..1000; binary grumpy."""
    rng = random.Random(seed)
    calls = {
        "candidate(customers=[1, 0, 1, 2, 1, 1, 7, 5], grumpy=[0, 1, 0, 1, 0, 1, 0, 1], minutes=3)",
        "candidate(customers=[1], grumpy=[0], minutes=1)",
    }
    while len(calls) < 600:
        size = rng.randint(1, 200)
        customers = [rng.randint(0, 1000) for _ in range(size)]
        grumpy = [rng.randint(0, 1) for _ in range(size)]
        minutes = rng.randint(1, size)
        calls.add(
            f"candidate(customers={customers!r}, grumpy={grumpy!r}, minutes={minutes})"
        )
    return sorted(calls)
