import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        m = rng.randint(1, 20)
        n = rng.randint(1, 20)
        grid = [[rng.randint(0, 1) for _ in range(n)] for _ in range(m)]
        key = tuple(map(tuple, grid))
        if key not in seen:
            seen.add(key)
            assert len(grid) == m and all(
                len(row) == n and all(v in (0, 1) for v in row) for row in grid
            )
            cases.append(f"candidate(grid={grid!r})")
    return cases
