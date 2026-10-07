import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            "candidate(grid = [[0,1,1,0],[1,1,1,1]])",
            "candidate(grid = [[1,1,1],[1,1,1]])",
            "candidate(grid = [[1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1],[0,1,0,0,1]])",
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
        matrix(p["grid"], 0, 1, 1, 1000, 100000)

    add(grid=[[1] * 1000 for _ in range(100)])
    add(grid=[[1] for _ in range(1000)])
    attempts = 0
    while len(calls) < 600:
        mode = attempts % 8
        attempts += 1
        r, c = rng.randint(1, 14), rng.randint(1, 14)
        grid = [
            [
                1
                if mode in (0, 1)
                else int(rng.random() < (0.85 if mode < 5 else 0.35))
                for _ in range(c)
            ]
            for _ in range(r)
        ]
        add(grid=grid)
    return list(calls)
