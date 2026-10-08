import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        b = kw["board"]
        n = len(b)
        assert 2 <= n <= 30 and all(len(row) == n and set(row) <= {0, 1} for row in b)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [
        {"board": [[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]},
        {"board": [[0, 1], [1, 0]]},
        {"board": [[1, 0], [1, 0]]},
    ] + [
        {"board": [[(i + j) % 2 for j in range(30)] for i in range(30)]},
        {"board": [[1] * 30 for _ in range(30)]},
    ]:
        add(**kw)
    while len(calls) < 600:
        n = rng.randint(2, 14)
        if len(calls) % 2 == 0:
            rows = list(range(n))
            cols = list(range(n))
            rng.shuffle(rows)
            rng.shuffle(cols)
            start = rng.randint(0, 1)
            b = [[(i + j + start) % 2 for j in cols] for i in rows]
        else:
            b = [[rng.randint(0, 1) for _ in range(n)] for _ in range(n)]
        add(board=b)
    return calls
