import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        n = rng.randint(1, 25)
        matrix = [[rng.randint(-100, 100) for _ in range(n)] for _ in range(n)]
        key = tuple(map(tuple, matrix))
        if key not in seen:
            seen.add(key)
            assert len(matrix) == n and all(
                len(row) == n and all(-100 <= v <= 100 for v in row) for row in matrix
            )
            cases.append(f"candidate(matrix={matrix!r})")
    return cases
