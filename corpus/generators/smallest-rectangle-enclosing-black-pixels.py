import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            'candidate(image = [["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]], x = 0, y = 2)',
            'candidate(image = [["1"]], x = 0, y = 0)',
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
        matrix(p["image"], "0", "1", 1, 100)
        m, n = len(p["image"]), len(p["image"][0])
        assert 0 <= p["x"] < m and 0 <= p["y"] < n and p["image"][p["x"]][p["y"]] == "1"
        black = {(i, j) for i in range(m) for j in range(n) if p["image"][i][j] == "1"}
        seen = {(p["x"], p["y"])}
        queue = list(seen)
        for i, j in queue:
            for a, b in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if (a, b) in black and (a, b) not in seen:
                    seen.add((a, b))
                    queue.append((a, b))
        assert seen == black

    add(image=[["1"] * 100 for _ in range(100)], x=99, y=99)
    attempts = 0
    while len(calls) < 600:
        attempts % 8
        attempts += 1
        m, n = rng.randint(1, 20), rng.randint(1, 20)
        x, y = rng.randrange(m), rng.randrange(n)
        black = {(x, y)}
        for _ in range(rng.randint(0, m * n * 3)):
            i, j = rng.choice(tuple(black))
            a, b = rng.choice(((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)))
            if 0 <= a < m and 0 <= b < n:
                black.add((a, b))
        image = [["1" if (i, j) in black else "0" for j in range(n)] for i in range(m)]
        add(image=image, x=x, y=y)
    return list(calls)
