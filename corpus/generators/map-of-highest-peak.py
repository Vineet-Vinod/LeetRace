import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: matrix dimensions1..1000 with at least one water; includes a 1000x1000 boundary."""
    rng = random.Random(seed)
    calls = {
        "candidate(isWater=[[0, 1], [0, 0]])",
        "candidate(isWater=[[0] * 100 for _ in range(99)] + [[1] + [0] * 99])",
        "candidate(isWater=[[0] * 1000 for _ in range(999)] + [[1] + [0] * 999])",
    }
    while len(calls) < 600:
        rows, cols = rng.randint(1, 30), rng.randint(1, 30)
        water = [[rng.randint(0, 1) for _ in range(cols)] for _ in range(rows)]
        water[rng.randrange(rows)][rng.randrange(cols)] = 1
        calls.add(f"candidate(isWater={water!r})")
    return sorted(calls)
