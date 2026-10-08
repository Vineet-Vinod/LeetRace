import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        rows = kwargs["statements"]
        n = len(rows)
        assert 2 <= n <= 15 and all(len(row) == n for row in rows)
        assert all(rows[i][i] == 2 for i in range(n)) and all(
            v in (0, 1, 2) for row in rows for v in row
        )
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(statements=[[2] * 15 for _ in range(15)])
    add(statements=[[2 if i == j else 0 for j in range(15)] for i in range(15)])
    add(statements=[[2 if i == j else 1 for j in range(15)] for i in range(15)])
    add(statements=[[2, 1, 2], [1, 2, 2], [2, 0, 2]])
    add(statements=[[2, 0], [0, 2]])
    while len(calls) < 600:
        n = rng.randint(2, 8)
        mode = len(calls) % 3
        statements = [
            [2 if a == b else rng.randrange(3) for b in range(n)] for a in range(n)
        ]
        if mode == 0:
            good = [rng.randrange(2) for _ in range(n)]
            statements = [
                [
                    2 if a == b else good[b] if good[a] else rng.randrange(3)
                    for b in range(n)
                ]
                for a in range(n)
            ]
        add(statements=statements)
    return calls
