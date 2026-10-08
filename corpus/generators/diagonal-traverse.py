def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    square = [[(r * 100 + c) % 100001 - 50000 for c in range(100)] for r in range(100)]
    cases = {
        "candidate(mat=[[-100000,100000]])",
        f"candidate(mat={square!r})",
    }
    while len(cases) < 600:
        rows, cols = rng.randint(1, 20), rng.randint(1, 20)
        mat = [[rng.randint(-100000, 100000) for _ in range(cols)] for _ in range(rows)]
        assert 1 <= rows * cols <= 10000
        assert all(-100000 <= value <= 100000 for row in mat for value in row)
        cases.add(f"candidate(mat={mat!r})")
    return sorted(cases)
