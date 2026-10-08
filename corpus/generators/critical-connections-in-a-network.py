import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        n, e = kwargs["n"], kwargs["connections"]
        assert 2 <= n <= 100000 and n - 1 <= len(e) <= 100000
        assert all(0 <= a < n and 0 <= b < n and a != b for a, b in e)
        assert len({tuple(sorted(edge)) for edge in e}) == len(e)
        adj = [[] for _ in range(n)]
        for a, b in e:
            adj[a].append(b)
            adj[b].append(a)
        visited = {0}
        stack = [0]
        while stack:
            for v in adj[stack.pop()]:
                if v not in visited:
                    visited.add(v)
                    stack.append(v)
        assert len(visited) == n
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(n=4, connections=[[0, 1], [1, 2], [2, 0], [1, 3]])
    add(n=2, connections=[[0, 1]])
    add(n=100000, connections=[[i, i + 1] for i in range(99999)])
    add(n=100000, connections=[[i, (i + 1) % 100000] for i in range(100000)])
    while len(calls) < 600:
        n = rng.randint(2, 35)
        e = {tuple(sorted((i, rng.randrange(i)))) for i in range(1, n)}
        if len(calls) % 3:
            for _ in range(n * 2):
                a, b = rng.sample(range(n), 2)
                e.add(tuple(sorted((a, b))))
        connections = [list(edge) for edge in sorted(e)]
        rng.shuffle(connections)
        for edge in connections:
            if rng.randrange(2):
                edge.reverse()
        add(n=n, connections=connections)
    return calls
