import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty matrices up to 300x300, values 0..10000, threshold 0..100000."""
    rng = random.Random(seed)
    calls = {
        "candidate(mat=[[1, 1, 3], [1, 1, 3]], threshold=4)",
        "candidate(mat=[[2, 2], [2, 2]], threshold=1)",
        "candidate(mat=[[10000] * 300 for _ in range(300)], threshold=100000)",
        "candidate(mat=[[0] * 300 for _ in range(300)], threshold=0)",
    }
    while len(calls) < 600:
        rows, cols = rng.randint(1, 60), rng.randint(1, 60)
        base = rng.choice([0, 1, 10000])
        mat = [
            [base if rng.random() < 0.7 else rng.randint(0, 10000) for _ in range(cols)]
            for _ in range(rows)
        ]
        threshold = rng.choice([0, 100000, rng.randint(0, 100000)])
        assert 1 <= len(mat) <= 300 and 1 <= len(mat[0]) <= 300
        assert all(
            len(row) == len(mat[0]) and all(0 <= value <= 10000 for value in row)
            for row in mat
        )
        assert 0 <= threshold <= 100000
        calls.add(f"candidate(mat={mat!r}, threshold={threshold})")
    return sorted(calls)
