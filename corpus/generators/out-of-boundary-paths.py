import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        m = rng.randint(1, 15)
        n = rng.randint(1, 15)
        moves = rng.randint(0, 50)
        row = rng.randrange(m)
        col = rng.randrange(n)
        key = (m, n, moves, row, col)
        if key not in seen:
            seen.add(key)
            assert (
                1 <= m <= 50
                and 1 <= n <= 50
                and 0 <= moves <= 50
                and 0 <= row < m
                and 0 <= col < n
            )
            cases.append(
                f"candidate(m={m}, n={n}, maxMove={moves}, startRow={row}, startColumn={col})"
            )
    return cases
