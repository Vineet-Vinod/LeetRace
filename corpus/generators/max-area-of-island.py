import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        rows = rng.randint(1, 20)
        cols = rng.randint(1, 20)
        grid = [[rng.randint(0, 1) for _ in range(cols)] for _ in range(rows)]
        key = tuple(map(tuple, grid))
        if key not in seen:
            seen.add(key)
            assert all(
                len(row) == cols and all(v in (0, 1) for v in row) for row in grid
            )
            cases.append(f"candidate(grid={grid!r})")
    return cases
