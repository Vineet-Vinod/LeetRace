import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: rectangular binary matrix dimensions 1..300; generated includes a 300x300 all-one boundary case."""
    rng = random.Random(seed)
    calls = {
        "candidate(matrix=[[1]])",
        "candidate(matrix=[[1, 1, 1], [1, 1, 1], [1, 1, 1]])",
        f"candidate(matrix={[[1] * 300 for _ in range(300)]!r})",
    }
    while len(calls) < 600:
        rows, cols = rng.randint(1, 25), rng.randint(1, 25)
        matrix = [[rng.randint(0, 1) for _ in range(cols)] for _ in range(rows)]
        calls.add(f"candidate(matrix={matrix!r})")
    return sorted(calls)
