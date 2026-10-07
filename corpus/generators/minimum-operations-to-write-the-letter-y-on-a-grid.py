import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        n = 2 * rng.randint(1, 15) + 1
        grid = [[rng.randint(0, 2) for _ in range(n)] for _ in range(n)]
        key = tuple(map(tuple, grid))
        if key not in seen:
            seen.add(key)
            assert (
                n % 2 == 1
                and n >= 3
                and all(
                    len(row) == n and all(v in (0, 1, 2) for v in row) for row in grid
                )
            )
            cases.append(f"candidate(grid={grid!r})")
    return cases
