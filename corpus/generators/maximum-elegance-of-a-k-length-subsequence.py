import random


def sample(r, turn):
    n = r.randint(1, 45)
    k = r.randint(1, n)
    a = [[r.choice([1, 10**9, r.randint(1, 30)]), r.randint(1, n)] for _ in range(n)]
    if turn % 4 == 0:
        a = [[r.randint(1, 50), 1] for _ in range(n)]
    return dict(items=a, k=k)


def validate(items, k):
    n = len(items)
    assert 1 <= k <= n <= 100000 and all(
        len(a) == 2 and 1 <= a[0] <= 10**9 and 1 <= a[1] <= n for a in items
    )


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

    add(items=[[3, 2], [5, 1], [10, 1]], k=2)
    add(items=[[3, 1], [3, 1], [2, 2], [5, 3]], k=3)
    add(items=[[1, 1], [2, 1], [3, 1]], k=3)
    add(items=[[10**9, i] for i in range(1, 100001)], k=100000)
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
