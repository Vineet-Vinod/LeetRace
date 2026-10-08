def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    maximum = [[1] * 100 for _ in range(100)]
    maximum[0][0] = 0
    cases = {
        "candidate(mat=[[0]])",
        f"candidate(mat={maximum!r})",
    }
    while len(cases) < 600:
        rows = rng.randint(1, 20)
        cols = rng.randint(1, 20)
        mat = [[rng.randint(0, 1) for _ in range(cols)] for _ in range(rows)]
        mat[rng.randrange(rows)][rng.randrange(cols)] = 0
        assert 1 <= rows * cols <= 10000
        assert any(0 in row for row in mat)
        cases.add(f"candidate(mat={mat!r})")
    return sorted(cases)
