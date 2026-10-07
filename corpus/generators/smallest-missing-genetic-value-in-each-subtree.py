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
    n = r.randint(2, 55)
    p = [-1] + [r.randrange(i) for i in range(1, n)]
    a = r.sample(range(1, 100001), n)
    if turn % 3 != 0:
        a = list(range(1, n + 1))
        r.shuffle(a)
    return dict(parents=p, nums=a)


def validate(parents, nums):
    n = len(nums)
    assert 2 <= n <= 100000 and len(parents) == n and parents[0] == -1
    assert len(set(nums)) == n and all(1 <= v <= 100000 for v in nums)
    assert all(0 <= parents[i] < n and parents[i] != i for i in range(1, n))
    check_tree(n, [[parents[i], i] for i in range(1, n)])


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

    add(parents=[-1, 0, 0, 2], nums=[1, 2, 3, 4])
    add(parents=[-1, 0, 1, 0, 3, 3], nums=[5, 4, 6, 2, 1, 3])
    add(parents=[-1, 2, 3, 0, 2, 4, 1], nums=[2, 3, 4, 5, 6, 7, 8])
    add(parents=[-1] + list(range(99999)), nums=list(range(100000, 0, -1)))
    turn = 0
    while len(calls) < 600:
        kwargs = sample(r, turn)
        turn += 1
        add(**kwargs)
    assert len(calls) == len(set(calls)) == 600
    return calls
