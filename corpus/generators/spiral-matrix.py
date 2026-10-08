def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])",
        "candidate(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])",
    }
    while len(cases) < 600:
        m, n = rng.randint(1, 10), rng.randint(1, 10)
        matrix = [[rng.randint(-100, 100) for _ in range(n)] for _ in range(m)]
        assert (
            1 <= m <= 10
            and 1 <= n <= 10
            and all(-100 <= x <= 100 for row in matrix for x in row)
        )
        cases.add(f"candidate(matrix={matrix!r})")
    return sorted(cases)
