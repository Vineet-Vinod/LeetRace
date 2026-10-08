import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            "candidate(n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5)",
            "candidate(n = 2, edges = [[1,2]], time = 3, change = 2)",
        ]
    )

    def add(**kwargs):
        validate(kwargs)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        calls[ast.unparse(ast.parse(call, mode="eval"))] = None

    def tree(n):
        return [[rng.randrange(i), i] for i in range(1, n)]

    def connected(n, extra=0):
        edges = {tuple(edge) for edge in tree(n)}
        while len(edges) < min(n * (n - 1) // 2, n - 1 + extra):
            a, b = sorted(rng.sample(range(n), 2))
            edges.add((a, b))
        return [[a + 1, b + 1] for a, b in sorted(edges)]

    def graph_valid(n, edges, minimum, maximum, connected_required=False, offset=0):
        assert minimum <= len(edges) <= maximum
        pairs = {tuple(sorted(edge)) for edge in edges}
        assert len(pairs) == len(edges)
        assert all(
            len(edge) == 2
            and edge[0] != edge[1]
            and all(offset <= x < n + offset for x in edge)
            for edge in edges
        )
        if connected_required:
            adj = [[] for _ in range(n)]
            for a, b in edges:
                adj[a - offset].append(b - offset)
                adj[b - offset].append(a - offset)
            seen = {0}
            queue = [0]
            for u in queue:
                for v in adj[u]:
                    if v not in seen:
                        seen.add(v)
                        queue.append(v)
            assert len(seen) == n

    def validate(p):
        n = p["n"]
        assert 2 <= n <= 10000
        graph_valid(n, p["edges"], n - 1, min(20000, n * (n - 1) // 2), True, 1)
        assert 1 <= p["time"] <= 1000 and 1 <= p["change"] <= 1000

    add(n=10000, edges=[[i, i + 1] for i in range(1, 10000)], time=1000, change=1000)
    add(n=10000, edges=connected(10000, 10001), time=1, change=1000)
    attempts = 0
    while len(calls) < 600:
        attempts % 8
        attempts += 1
        n = rng.randint(2, 30)
        add(
            n=n,
            edges=connected(n, rng.randint(0, 2 * n)),
            time=rng.randint(1, 1000),
            change=rng.randint(1, 1000),
        )
    return list(calls)
