import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: rectangular board; each dimension 3..50; cell types 1..2000."""
    rng = random.Random(seed)
    calls = {
        "candidate(board=[[1, 3, 5, 5, 2], [3, 4, 3, 3, 1], [3, 2, 4, 5, 2], [2, 4, 4, 5, 5], [1, 4, 4, 1, 1]])"
    }
    while len(calls) < 600:
        rows, cols = rng.randint(3, 12), rng.randint(3, 12)
        board = [[rng.randint(1, 8) for _ in range(cols)] for _ in range(rows)]
        calls.add(f"candidate(board={board!r})")
    return sorted(calls)
