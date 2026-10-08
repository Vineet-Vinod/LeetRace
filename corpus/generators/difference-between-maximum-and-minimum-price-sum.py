import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        n, edges, price = data["n"], data["edges"], data["price"]
        assert 1 <= n <= 100000 and len(edges) == n - 1 and len(price) == n
        assert all(1 <= x <= 100000 for x in price)
        parent = list(range(n))

        def root(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for edge in edges:
            assert len(edge) == 2
            u, v = edge
            assert 0 <= u < n and 0 <= v < n and root(u) != root(v)
            parent[root(u)] = root(v)
        # n-1 acyclic edges on n vertices prove connectivity.
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [
        {
            "n": 6,
            "edges": [[0, 1], [1, 2], [1, 3], [3, 4], [3, 5]],
            "price": [9, 8, 7, 6, 10, 5],
        },
        {"n": 3, "edges": [[0, 1], [1, 2]], "price": [1, 1, 1]},
    ]:
        add(**example)
    add(n=1, edges=[], price=[100000])
    add(n=100000, edges=[[i - 1, i] for i in range(1, 100000)], price=[100000] * 100000)
    add(n=100000, edges=[[0, i] for i in range(1, 100000)], price=[1] * 100000)
    while len(calls) < 600:
        n = rng.randint(1, 50)
        mode = len(calls) % 3
        edges = [
            [(i - 1 if mode == 0 else 0 if mode == 1 else rng.randrange(i)), i]
            for i in range(1, n)
        ]
        price = [rng.randint(1, 100000) for _ in range(n)]
        rng.shuffle(edges)
        add(n=n, edges=edges, price=price)
    assert len(calls) == 600
    return calls
