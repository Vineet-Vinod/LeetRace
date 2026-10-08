import random


def sample(r, turn):
    n = r.randint(1, 15)
    e = [
        [a, b, r.randint(0, 8)]
        for a in range(n)
        for b in range(a + 1, n)
        if r.random() < 0.2
    ]
    return dict(edges=e, maxMoves=r.choice([0, 1000000000, r.randint(1, 30)]), n=n)


def validate(edges, maxMoves, n):
    assert (
        1 <= n <= 3000
        and 0 <= maxMoves <= 10**9
        and len(edges) <= min(n * (n - 1) // 2, 10000)
    )
    assert all(0 <= a < b < n and 0 <= c <= 10000 for a, b, c in edges)
    assert len({(a, b) for a, b, c in edges}) == len(edges)


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

    add(edges=[[0, 1, 10], [0, 2, 1], [1, 2, 2]], maxMoves=6, n=3)
    add(edges=[[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]], maxMoves=10, n=4)
    add(edges=[[1, 2, 4], [1, 4, 5], [1, 3, 1], [2, 3, 4], [3, 4, 5]], maxMoves=17, n=5)
    pairs = [(i - 1, i) for i in range(1, 3000)]
    pairs += [(a, b) for a in range(10) for b in range(a + 2, 3000)][:7001]
    add(edges=[[a, b, 10000] for a, b in pairs], maxMoves=10**9, n=3000)
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
