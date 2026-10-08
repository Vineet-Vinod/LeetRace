import random


def check_connected(n, edges):
    adj = [[] for _ in range(n)]
    for e in edges:
        a, b = e[:2]
        assert 0 <= a < n and 0 <= b < n and a != b
        adj[a].append(b)
        adj[b].append(a)
    visited = {0}
    queue = [0]
    for a in queue:
        for b in adj[a]:
            if b not in visited:
                visited.add(b)
                queue.append(b)
    assert len(visited) == n


def sample(r, turn):
    n = r.randint(2, 9)
    pairs = {(r.randrange(i), i) for i in range(1, n)}
    for a in range(n):
        for b in range(a + 1, n):
            if r.random() < 0.3:
                pairs.add((a, b))
    e = [[a, b, r.choice([1, 2, 3, r.randint(1, 1000)])] for a, b in sorted(pairs)]
    r.shuffle(e)
    return dict(n=n, edges=e)


def validate(n, edges):
    assert 2 <= n <= 100 and 1 <= len(edges) <= min(200, n * (n - 1) // 2)
    assert all(0 <= a < b < n and 1 <= w <= 1000 for a, b, w in edges)
    assert len({(a, b) for a, b, w in edges}) == len(edges)
    check_connected(n, edges)


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
        n=5,
        edges=[
            [0, 1, 1],
            [1, 2, 1],
            [2, 3, 2],
            [0, 3, 2],
            [0, 4, 3],
            [3, 4, 3],
            [1, 4, 6],
        ],
    )
    add(n=4, edges=[[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]])
    e = [[i - 1, i, 1000] for i in range(1, 100)]
    e += [[0, i, 1] for i in range(2, 100)] + [[1, 99, 2], [2, 99, 3], [3, 99, 4]]
    add(n=100, edges=e)
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
