import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            "candidate(grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]])",
            "candidate(grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]])",
        ]
    )

    def add(**kwargs):
        validate(kwargs)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        calls[ast.unparse(ast.parse(call, mode="eval"))] = None

    def matrix(a, lo, hi, minimum=1, maximum=1000, cells=1000000):
        assert minimum <= len(a) <= maximum and minimum <= len(a[0]) <= maximum
        assert len(a) * len(a[0]) <= cells
        assert all(
            len(row) == len(a[0]) and all(lo <= x <= hi for x in row) for row in a
        )

    def validate(p):
        matrix(p["grid"], 0, 100, 2, 70)

    add(grid=[[100] * 70 for _ in range(70)])
    add(grid=[[0, 0], [0, 0]])
    attempts = 0
    while len(calls) < 600:
        mode = attempts % 8
        attempts += 1
        r, c = rng.randint(2, 8), rng.randint(2, 8)
        grid = [
            [
                rng.randint(0, 100 if mode == 0 else 8) if mode != 1 else 0
                for _ in range(c)
            ]
            for _ in range(r)
        ]
        if mode == 2:
            for i in range(r):
                grid[i][min(i, c - 1)] = 100
        add(grid=grid)
    return list(calls)
