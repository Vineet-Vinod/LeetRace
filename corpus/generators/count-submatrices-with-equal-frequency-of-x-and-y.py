import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases, seen = [], set()
    while len(cases) < 600:
        rows = rng.randint(1, 12)
        cols = rng.randint(1, 12)
        grid = [[rng.choice(["X", "Y", "."]) for _ in range(cols)] for _ in range(rows)]
        key = tuple(tuple(row) for row in grid)
        if key not in seen:
            seen.add(key)
            assert all(len(row) == cols for row in grid) and all(
                v in {"X", "Y", "."} for row in grid for v in row
            )
            cases.append(f"candidate(grid={grid!r})")
    return cases
