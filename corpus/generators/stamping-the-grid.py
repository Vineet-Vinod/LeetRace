import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        g = d["grid"]
        r, c = len(g), len(g[0])
        assert 1 <= r <= 100000 and 1 <= c <= 100000 and 1 <= r * c <= 200000
        assert (
            all(len(row) == c and all(v in (0, 1) for v in row) for row in g)
            and 1 <= d["stampHeight"] <= 100000
            and 1 <= d["stampWidth"] <= 100000
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

    add(
        grid=[[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]],
        stampHeight=4,
        stampWidth=3,
    )
    add(
        grid=[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
        stampHeight=2,
        stampWidth=2,
    )
    add(grid=[[0] * 100000, [0] * 100000], stampHeight=2, stampWidth=100000)
    add(grid=[[0, 0] for _ in range(100000)], stampHeight=100000, stampWidth=2)
    add(grid=[[1]], stampHeight=100000, stampWidth=100000)
    t = 0
    while len(calls) < 600:
        r, c = rng.randint(1, 12), rng.randint(1, 12)
        h, w = rng.randint(1, 15), rng.randint(1, 15)
        g = [[rng.randrange(2) for _ in range(c)] for _ in range(r)]
        if t % 3 == 0:
            h, w = rng.randint(1, r), rng.randint(1, c)
            g = [[1] * c for _ in range(r)]
            for _ in range(rng.randint(1, 5)):
                x, y = rng.randint(0, r - h), rng.randint(0, c - w)
                for i in range(x, x + h):
                    for j in range(y, y + w):
                        g[i][j] = 0
        add(grid=g, stampHeight=h, stampWidth=w)
        t += 1
    return calls
