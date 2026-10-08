import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(grid):
        n = len(grid)
        assert 1 <= n <= 100 and all(len(row) == n for row in grid)
        assert all(0 <= v <= 10**9 for row in grid for v in row)

    add(grid=[[0]])
    while len(calls) < 598:
        n = rng.randint(1, 8)
        mode = len(calls) % 4
        grid = [[rng.randint(0, 30) for _ in range(n)] for _ in range(n)]
        if mode == 0:
            grid = [
                [0 if rng.random() < 0.8 else rng.randint(1, 10**9) for _ in range(n)]
                for _ in range(n)
            ]
        if mode == 1:
            grid = [[rng.randint(0, 1) for _ in range(n)] for _ in range(n)]
        add(grid=grid)
    calls["candidate(grid=[[0]*100 for _ in range(100)])"] = None
    calls["candidate(grid=[[1000000000]*100 for _ in range(100)])"] = None
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
