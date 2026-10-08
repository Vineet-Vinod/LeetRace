import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: ages length1..20000, values1..120."""
    rng = random.Random(seed)
    calls = {
        "candidate(ages=[16, 16])",
        "candidate(ages=[16, 17, 18])",
        "candidate(ages=[20, 30, 100, 110, 120])",
    }
    while len(calls) < 600:
        ages = [rng.randint(1, 120) for _ in range(rng.randint(1, 150))]
        calls.add(f"candidate(ages={ages!r})")
    return sorted(calls)
