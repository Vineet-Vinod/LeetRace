"""Seeded legal inputs, including original examples and maximum-size boundaries."""

import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def validate(kw):
        g = kw["grid"]
        n = len(g)
        assert 1 <= n <= 500 and all(
            len(row) == n and all(v in (0, 1) for v in row) for row in g
        )

    def add_call(call):
        kw = eval(call, {"candidate": lambda **kwargs: kwargs})
        validate(kw)
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        if key not in seen:
            seen.add(key)
            calls.append(call)

    def factory(index):
        n = rng.randint(1, 12)
        prob = rng.choice([0.1, 0.4, 0.7, 0.95])
        return dict(
            grid=[[int(rng.random() < prob) for _ in range(n)] for _ in range(n)]
        )

    for call in [
        "candidate(grid = [[1,0],[0,1]])",
        "candidate(grid = [[1,1],[1,0]])",
        "candidate(grid = [[1,1],[1,1]])",
        "candidate(grid=[[1]*500 for _ in range(500)])",
        "candidate(grid=[[0]*500 for _ in range(500)])",
        "candidate(grid=[[(i+j)%2 for j in range(500)] for i in range(500)])",
        "candidate(grid=[[0]])",
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
