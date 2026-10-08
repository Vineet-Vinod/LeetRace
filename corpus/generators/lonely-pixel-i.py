def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    diagonal = [["B" if r == c else "W" for c in range(500)] for r in range(500)]
    cases = {
        "candidate(picture=[['W','W','B'],['W','B','W'],['B','W','W']])",
        "candidate(picture=[['B','B','B'],['B','B','W'],['B','B','B']])",
        f"candidate(picture={diagonal!r})",
    }
    while len(cases) < 600:
        m, n = rng.randint(1, 50), rng.randint(1, 50)
        picture = [["W"] * n for _ in range(m)]
        count = rng.randint(0, min(m, n))
        rows = rng.sample(range(m), count)
        cols = rng.sample(range(n), count)
        rng.shuffle(cols)
        for row, col in zip(rows, cols):
            picture[row][col] = "B"
        assert 1 <= m <= 500 and 1 <= n <= 500
        assert all(value in {"B", "W"} for row in picture for value in row)
        cases.add(f"candidate(picture={picture!r})")
    return sorted(cases)
