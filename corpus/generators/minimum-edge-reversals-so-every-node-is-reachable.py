import random

EXAMPLES = [
    "candidate(n=4, edges=[[2, 0], [2, 1], [1, 3]])",
    "candidate(n=3, edges=[[1, 2], [2, 0]])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(n, edges):
        assert 2 <= n <= 100000 and len(edges) == n - 1
        parent = list(range(n))

        def find(a):
            while parent[a] != a:
                parent[a] = parent[parent[a]]
                a = parent[a]
            return a

        for u, v in edges:
            assert 0 <= u < n and 0 <= v < n and u != v
            a, b = find(u), find(v)
            assert a != b
            parent[a] = b
        # n-1 acyclic edges imply connectivity.
        emit(f"candidate(n={n}, edges={edges!r})")

    add(100000, [[i, i + 1] for i in range(99999)])
    add(100000, [[i, 0] for i in range(1, 100000)])
    while len(calls) < 600:
        n = rng.randint(2, 45)
        edges = []
        for v in range(1, n):
            u = rng.randrange(v)
            edges.append([u, v] if rng.random() < 0.5 else [v, u])
        rng.shuffle(edges)
        add(n, edges)
    return calls
