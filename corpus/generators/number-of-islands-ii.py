import random


def sample(r, turn):
    m, n = r.randint(1, 10), r.randint(1, 10)
    p = [[r.randrange(m), r.randrange(n)] for _ in range(r.randint(1, 60))]
    return dict(m=m, n=n, positions=p)


def validate(m, n, positions):
    assert (
        1 <= m <= 10000
        and 1 <= n <= 10000
        and 1 <= m * n <= 10000
        and 1 <= len(positions) <= 10000
    )
    assert all(len(p) == 2 and 0 <= p[0] < m and 0 <= p[1] < n for p in positions)


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

    add(m=3, n=3, positions=[[0, 0], [0, 1], [1, 2], [2, 1]])
    add(m=1, n=1, positions=[[0, 0]])
    add(m=10000, n=1, positions=[[i, 0] for i in range(10000)])
    add(m=1, n=10000, positions=[[0, i] for i in range(10000)])
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
