def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    max_n = 200
    cases = set()

    def grid_for_order(order: list[int]) -> list[list[int]]:
        n = len(order)
        return [[1] * (n - trailing) + [0] * trailing for trailing in order]

    cases.add(f"candidate(grid={grid_for_order(list(range(max_n - 1, -1, -1)))!r})")
    cases.add(f"candidate(grid={grid_for_order(list(range(max_n)))!r})")
    cases.add("candidate(grid=[[0, 0, 1], [1, 1, 0], [1, 0, 0]])")
    cases.add("candidate(grid=[[0, 1], [0, 1]])")
    while len(cases) < 600:
        n = rng.randint(1, 80)
        if rng.random() < 0.7:
            order = list(range(n))
            rng.shuffle(order)
            grid = grid_for_order(order)
        else:
            grid = [[rng.randrange(2) for _ in range(n)] for _ in range(n)]
        assert 1 <= len(grid) <= 200 and all(len(row) == len(grid) for row in grid)
        assert all(value in (0, 1) for row in grid for value in row)
        cases.add(f"candidate(grid={grid!r})")
    return sorted(cases)
