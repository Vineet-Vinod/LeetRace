import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        v = kw["values"]
        m, n = len(v), len(v[0])
        assert 1 <= m <= 10 and 1 <= n <= 10000
        assert all(
            len(row) == n
            and all(1 <= x <= 10**6 for x in row)
            and row == sorted(row, reverse=True)
            for row in v
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
        {"values": [[8, 5, 2], [6, 4, 1], [9, 7, 3]]},
        {"values": [[10, 8, 6, 4, 2], [9, 7, 5, 3, 2]]},
    ] + [{"values": [[10**6] * 10000 for _ in range(10)]}, {"values": [[1]]}]:
        add(**kw)
    while len(calls) < 600:
        m, n = rng.randint(1, 6), rng.randint(1, 15)
        v = [
            sorted([rng.randint(1, 100) for _ in range(n)], reverse=True)
            for _ in range(m)
        ]
        add(values=v)
    return calls
