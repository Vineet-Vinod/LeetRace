import random


def sample(r, turn):
    m, n = r.randint(1, 8), r.randint(1, 8)
    g = [[r.randint(1, 6) for _ in range(n)] for _ in range(m)]
    if turn % 2 == 0:
        g = [[1] * n for _ in range(m)]
        for color in range(2, r.randint(3, 10)):
            top, bottom = sorted([r.randrange(m), r.randrange(m)])
            left, right = sorted([r.randrange(n), r.randrange(n)])
            for a in range(top, bottom + 1):
                for b in range(left, right + 1):
                    g[a][b] = color
    return dict(targetGrid=g)


def validate(targetGrid):
    m, n = len(targetGrid), len(targetGrid[0])
    assert 1 <= m <= 60 and 1 <= n <= 60 and all(len(row) == n for row in targetGrid)
    assert all(1 <= v <= 60 for row in targetGrid for v in row)


def generate(seed: int = 0) -> list[str]:
    r = random.Random(seed)
    calls = []
    seen = set()

    def add(**kwargs):
        validate(**kwargs)
        parts = []
        for key, value in kwargs.items():
            expression = repr(value)
            parts.append(key + "=" + expression)
        call = "candidate(" + ", ".join(parts) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(targetGrid=[[1, 1, 1, 1], [1, 2, 2, 1], [1, 2, 2, 1], [1, 1, 1, 1]])
    add(targetGrid=[[1, 1, 1, 1], [1, 1, 3, 3], [1, 1, 3, 4], [5, 5, 1, 4]])
    add(targetGrid=[[1, 2, 1], [2, 1, 2], [1, 2, 1]])
    add(targetGrid=[[r + 1] * 60 for r in range(60)])
    add(targetGrid=[[1 + (r + c) % 2 for c in range(60)] for r in range(60)])
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
