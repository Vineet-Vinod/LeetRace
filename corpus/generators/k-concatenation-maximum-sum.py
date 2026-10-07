import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: arr length1..10^5, values -10^4..10^4, k1..10^5."""
    rng = random.Random(seed)
    calls = {"candidate(arr=[1, 2], k=3)", "candidate(arr=[-1, -2], k=7)"}
    while len(calls) < 600:
        arr = [rng.randint(-10_000, 10_000) for _ in range(rng.randint(1, 100))]
        k = rng.randint(1, 100_000)
        calls.add(f"candidate(arr={arr!r}, k={k})")
    return sorted(calls)
