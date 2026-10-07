import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: distinct positions in1..10^9; 2<=m<=n<=10^5."""
    rng = random.Random(seed)
    calls = {
        "candidate(position=[1, 2, 3, 4, 7], m=3)",
        "candidate(position=[5, 4, 3, 2, 1, 1000000000], m=2)",
    }
    while len(calls) < 600:
        position = rng.sample(range(1, 10**9 + 1), rng.randint(2, 50))
        m = rng.randint(2, len(position))
        calls.add(f"candidate(position={position!r}, m={m})")
    return sorted(calls)
