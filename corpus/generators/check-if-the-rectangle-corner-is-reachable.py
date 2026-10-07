"""Seeded legal inputs, including original examples and maximum-size boundaries."""

import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def validate(kw):
        assert 3 <= kw["xCorner"] <= 10**9 and 3 <= kw["yCorner"] <= 10**9
        assert 1 <= len(kw["circles"]) <= 1000 and all(
            len(c) == 3 and all(1 <= v <= 10**9 for v in c) for c in kw["circles"]
        )

    def add_call(call):
        kw = eval(call, {"candidate": lambda **kwargs: kwargs})
        validate(kw)
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        if key not in seen:
            seen.add(key)
            calls.append(call)

    def factory(index):
        x, y = rng.randint(3, 60), rng.randint(3, 60)
        mode = index % 4
        if mode == 0:
            circles = [
                [x + rng.randint(2, 30), y + rng.randint(2, 30), 1]
                for _ in range(rng.randint(1, 12))
            ]
        elif mode == 1:
            circles = [
                [rng.randint(1, x), rng.randint(1, y), rng.randint(1, max(x, y))]
                for _ in range(rng.randint(1, 8))
            ]
        elif mode == 2:
            circles = [
                [rng.randint(1, 2 * x), rng.randint(1, 2 * y), rng.randint(1, 10)]
                for _ in range(rng.randint(1, 12))
            ]
        else:
            circles = [[1, 1, 1], [x + rng.randint(2, 20), y + 1, 1]]
        return dict(xCorner=x, yCorner=y, circles=circles)

    for call in [
        "candidate(xCorner = 3, yCorner = 4, circles = [[2,1,1]])",
        "candidate(xCorner = 3, yCorner = 3, circles = [[1,1,2]])",
        "candidate(xCorner = 3, yCorner = 3, circles = [[2,1,1],[1,2,1]])",
        "candidate(xCorner = 4, yCorner = 4, circles = [[5,5,1]])",
        "candidate(xCorner=10**9,yCorner=10**9,circles=[[10**9,1,1]])",
        "candidate(xCorner=1000,yCorner=1000,circles=[[2000+i,2000,1] for i in range(1000)])",
        "candidate(xCorner=3,yCorner=3,circles=[[3,3,1]])",
        "candidate(xCorner=1000000000,yCorner=1000000000,circles=[[1,1,1000000000]])",
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
