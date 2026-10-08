import random


def sample(r, turn):
    n = r.randint(1, 9)
    order = r.sample(range(1, n + 1), n)
    e = [
        [order[i], order[j]]
        for i in range(n)
        for j in range(i + 1, n)
        if r.random() < 0.3
    ]
    return dict(n=n, relations=e, k=r.randint(1, n))


def validate(n, relations, k):
    assert 1 <= k <= n <= 15 and len(relations) <= n * (n - 1) // 2
    assert len({tuple(e) for e in relations}) == len(relations) and all(
        1 <= a <= n and 1 <= b <= n and a != b for a, b in relations
    )
    ind = [0] * n
    adj = [[] for _ in range(n)]
    for a, b in relations:
        adj[a - 1].append(b - 1)
        ind[b - 1] += 1
    queue = [i for i in range(n) if ind[i] == 0]
    for a in queue:
        for b in adj[a]:
            ind[b] -= 1
            if ind[b] == 0:
                queue.append(b)
    assert len(queue) == n


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

    add(n=4, relations=[[2, 1], [3, 1], [1, 4]], k=2)
    add(n=5, relations=[[2, 1], [3, 1], [4, 1], [1, 5]], k=2)
    add(n=15, relations=[[i, j] for i in range(1, 16) for j in range(i + 1, 16)], k=15)
    add(n=15, relations=[], k=7)
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
