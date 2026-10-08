import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: exactly four digits, each0..9."""
    rng = random.Random(seed)
    calls = {"candidate(arr=[1, 2, 3, 4])", "candidate(arr=[5, 5, 5, 5])"}
    while len(calls) < 600:
        arr = [rng.randint(0, 9) for _ in range(4)]
        calls.add(f"candidate(arr={arr!r})")
    return sorted(calls)
