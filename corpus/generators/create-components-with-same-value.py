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


def check_tree(n, edges):
    assert len(edges) == n - 1
    check_connected(n, edges)


def sample(r, turn):
    n = r.randint(1, 30)
    edges = [[r.randrange(i), i] for i in range(1, n)]
    a = [r.randint(1, 50) for _ in range(n)]
    if turn % 3 == 0:
        a = [r.randint(1, 50)] * n
    return dict(nums=a, edges=edges)


def validate(nums, edges):
    assert 1 <= len(nums) <= 20000 and all(1 <= v <= 50 for v in nums)
    assert len(edges) == len(nums) - 1
    check_tree(len(nums), edges)


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

    add(nums=[6, 2, 2, 2, 6], edges=[[0, 1], [1, 2], [1, 3], [3, 4]])
    add(nums=[2], edges=[])
    add(nums=[50] * 20000, edges=[[i - 1, i] for i in range(1, 20000)])
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
