import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        grid = values["grid"]
        m, n = len(grid), len(grid[0])
        assert (
            1 <= m <= 100000
            and 1 <= n <= 100000
            and 2 <= m * n <= 100000
            and all(len(row) == n and all(x in (0, 1) for x in row) for row in grid)
        )
        assert grid[0][0] == grid[-1][-1] == 0
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    emit(grid=[[0, 0]])
    emit(grid=[[0] + [1] * 99998 + [0]])
    emit(grid=[[0] for _ in range(100000)])
    emit(grid=[[0, 1, 1], [1, 1, 0], [1, 1, 0]])
    while len(calls) < 600:
        m, n = rng.randint(1, 12), rng.randint(2, 12)
        probability = rng.choice([0.2, 0.5, 0.8])
        grid = [[int(rng.random() < probability) for _ in range(n)] for _ in range(m)]
        grid[0][0] = grid[-1][-1] = 0
        if len(calls) % 3 == 0:
            grid[0] = [0] * n
            for row in grid:
                row[-1] = 0
        emit(grid=grid)
    return calls
