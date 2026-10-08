import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: price length2..10^5, positive values1..10^9; duplicate prices allowed."""
    rng = random.Random(seed)
    calls = {
        "candidate(price=[13, 5, 1, 8, 21, 2], k=3)",
        "candidate(price=[7, 7, 7, 7], k=2)",
    }
    while len(calls) < 600:
        price = [rng.randint(1, 10**9) for _ in range(rng.randint(2, 100))]
        k = rng.randint(2, len(price))
        calls.add(f"candidate(price={price!r}, k={k})")
    return sorted(calls)
