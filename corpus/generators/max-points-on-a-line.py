import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            "candidate(points = [[1,1],[2,2],[3,3]])",
            "candidate(points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])",
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

    def validate(p):
        assert 1 <= len(p["points"]) <= 300
        assert all(
            len(q) == 2 and all(-10000 <= v <= 10000 for v in q) for q in p["points"]
        )
        assert len({tuple(q) for q in p["points"]}) == len(p["points"])

    add(points=[[i, 2 * i] for i in range(300)])
    add(points=[[-10000, -10000], [-10000, 10000], [10000, -10000], [10000, 10000]])
    attempts = 0
    while len(calls) < 600:
        mode = attempts % 8
        attempts += 1
        n = rng.randint(1, 25)
        points = set()
        if mode < 3:
            slope = rng.randint(-5, 5)
            base = rng.randint(-20, 20)
            points = {(i, slope * i + base) for i in range(n)}
        else:
            while len(points) < n:
                points.add((rng.randint(-30, 30), rng.randint(-30, 30)))
        add(points=[list(q) for q in sorted(points)])
    return list(calls)
