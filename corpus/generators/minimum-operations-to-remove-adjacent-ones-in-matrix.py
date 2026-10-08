import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def valid(grid):
        return (
            1 <= len(grid) <= 300
            and 1 <= len(grid[0]) <= 300
            and all(
                len(row) == len(grid[0]) and all(x in (0, 1) for x in row)
                for row in grid
            )
        )

    def emit(**args):
        assert valid(**args), args
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in args.items()) + ")"
        calls[call] = None

    for grid in [
        [[1]],
        [[0]],
        [[1, 1]],
        [[1, 1, 0], [0, 1, 1], [1, 1, 1]],
        [[0, 1], [1, 0]],
        [[1] * 300 for _ in range(300)],
        [[int((r + c) % 2 == 0) for c in range(300)] for r in range(300)],
        [[0] * 300 for _ in range(300)],
    ]:
        emit(grid=grid)
    while len(calls) < 600:
        m, n = rng.randint(1, 7), rng.randint(1, 7)
        density = rng.choice([0.15, 0.4, 0.7, 0.95])
        grid = [[int(rng.random() < density) for _ in range(n)] for _ in range(m)]
        emit(grid=grid)
    assert len(calls) == 600
    return list(calls)
