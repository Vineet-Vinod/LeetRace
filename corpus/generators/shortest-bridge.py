def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        size = rng.randint(2, 20)
        first = (rng.randrange(size), rng.randrange(size))
        second = (rng.randrange(size), rng.randrange(size))
        if (
            first == second
            or abs(first[0] - second[0]) + abs(first[1] - second[1]) == 1
        ):
            continue
        grid = [[0] * size for _ in range(size)]
        grid[first[0]][first[1]] = 1
        grid[second[0]][second[1]] = 1
        assert sum(map(sum, grid)) == 2
        cases.add(f"candidate(grid={grid!r})")
    return sorted(cases)
