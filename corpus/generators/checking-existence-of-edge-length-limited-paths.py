import random


def sample(r, turn):
    n = r.randint(2, 25)
    e = []
    for _ in range(r.randint(1, 65)):
        a, b = r.sample(range(n), 2)
        e.append([a, b, r.choice([1, 2, 5, 10, 1000000000, r.randint(1, 100)])])
    q = []
    for _ in range(r.randint(1, 30)):
        a, b = r.sample(range(n), 2)
        q.append([a, b, r.choice([1, 2, 5, 10, 1000000000, r.randint(1, 100)])])
    return dict(n=n, edgeList=e, queries=q)


def validate(n, edgeList, queries):
    assert (
        2 <= n <= 100000
        and 1 <= len(edgeList) <= 100000
        and 1 <= len(queries) <= 100000
    )
    assert all(
        len(e) == 3
        and 0 <= e[0] < n
        and 0 <= e[1] < n
        and e[0] != e[1]
        and 1 <= e[2] <= 10**9
        for e in edgeList + queries
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

    add(
        n=3,
        edgeList=[[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]],
        queries=[[0, 1, 2], [0, 2, 5]],
    )
    add(
        n=5,
        edgeList=[[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]],
        queries=[[0, 4, 14], [1, 4, 13]],
    )
    add(
        n=100000,
        edgeList=[[i, i + 1, 10**9] for i in range(99999)] + [[0, 99999, 1]],
        queries=[[0, i + 1, 10**9] for i in range(99999)] + [[0, 99999, 1]],
    )
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
