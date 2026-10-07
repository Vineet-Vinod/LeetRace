import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        g = d["grid"]
        assert (
            1 <= len(g) <= 50
            and 1 <= len(g[0]) <= 50
            and all(
                len(row) == len(g[0]) and all(v in (0, 1) for v in row) for row in g
            )
        )

    def add(**kwargs):
        valid(kwargs)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(grid=[[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 1]])
    add(grid=[[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]])
    add(grid=[[1] * 50 for _ in range(50)])
    add(grid=[[(i + j) % 2 for j in range(50)] for i in range(50)])
    add(grid=[[0] * 50 for _ in range(50)])
    t = 0
    while len(calls) < 600:
        r, c = rng.randint(1, 15), rng.randint(1, 15)
        p = rng.choice([0.1, 0.3, 0.6, 0.9])
        g = [[int(rng.random() < p) for _ in range(c)] for _ in range(r)]
        add(grid=g)
        t += 1
    return calls
