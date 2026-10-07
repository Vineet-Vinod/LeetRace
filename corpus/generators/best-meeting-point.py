"""Seeded legal inputs, including original examples and maximum-size boundaries."""

import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def validate(kw):
        grid = kw["grid"]
        m = len(grid)
        n = len(grid[0])
        assert (
            1 <= m <= 200
            and 1 <= n <= 200
            and all(len(row) == n and all(v in (0, 1) for v in row) for row in grid)
        )
        assert sum(map(sum, grid)) >= 2

    def add_call(call):
        kw = eval(call, {"candidate": lambda **kwargs: kwargs})
        validate(kw)
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        if key not in seen:
            seen.add(key)
            calls.append(call)

    def factory(index):
        m, n = rng.randint(1, 12), rng.randint(2, 12)
        grid = [
            [int(rng.random() < rng.choice([0.1, 0.5, 0.9])) for _ in range(n)]
            for _ in range(m)
        ]
        grid[0][0] = grid[-1][-1] = 1
        return dict(grid=grid)

    for call in [
        "candidate(grid = [[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]])",
        "candidate(grid = [[1,1]])",
        "candidate(grid=[[1]*200 for _ in range(200)])",
        "candidate(grid=[[1,1]])",
    ]:
        add_call(call)
    index = 0
    while len(calls) < 600:
        kw = factory(index)
        add_call(
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        index += 1
    assert len(calls) == len(set(calls)) == 600
    return calls
