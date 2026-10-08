import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: k1..10^15; x1..8."""
    rng = random.Random(seed)
    calls = {"candidate(k=9, x=1)", "candidate(k=7, x=2)"}
    while len(calls) < 600:
        calls.add(f"candidate(k={rng.randint(1, 10**15)}, x={rng.randint(1, 8)})")
    return sorted(calls)
