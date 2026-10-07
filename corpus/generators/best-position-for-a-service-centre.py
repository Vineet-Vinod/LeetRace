import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        p = kw["positions"]
        assert 1 <= len(p) <= 50
        assert all(
            len(v) == 2 and all(isinstance(x, int) and 0 <= x <= 100 for x in v)
            for v in p
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [
        {"positions": [[0, 1], [1, 0], [1, 2], [2, 1]]},
        {"positions": [[1, 1], [3, 3]]},
    ] + [
        {"positions": [[0, 0]] * 50},
        {"positions": [[i * 2, i * 2] for i in range(50)]},
        {"positions": [[0, 100], [100, 0]]},
    ]:
        add(**kw)
    while len(calls) < 600:
        mode = len(calls) % 5
        n = rng.randint(1, 6)
        if mode == 0:
            x, y = rng.randrange(101), rng.randrange(101)
            p = [[x, y]] * n
        elif mode == 1:
            p = [[rng.randrange(101), 0] for _ in range(n)]
        elif mode == 2:
            p = [[0, 0], [100, 100], [0, 100], [100, 0]] + [
                [rng.randrange(101), rng.randrange(101)]
            ]
        else:
            p = [[rng.randrange(101), rng.randrange(101)] for _ in range(n)]
        add(positions=p)
    return calls
