import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        coins, edges = kwargs["coins"], kwargs["edges"]
        n = len(coins)
        assert (
            1 <= n <= 30000 and len(edges) == n - 1 and all(x in (0, 1) for x in coins)
        )
        assert all(0 <= a < n and 0 <= b < n and a != b for a, b in edges)
        parent = list(range(n))

        def find(v: int) -> int:
            while parent[v] != v:
                parent[v] = parent[parent[v]]
                v = parent[v]
            return v

        for a, b in edges:
            ra, rb = find(a), find(b)
            assert ra != rb, "A valid tree cannot contain a cycle or repeated edge."
            parent[ra] = rb
        assert len(edges) == n - 1 and len({find(v) for v in range(n)}) == 1
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(coins=[1] * 30000, edges=[[v, v - 1] for v in range(1, 30000)])
    add(coins=[0] * 30000, edges=[[v, 0] for v in range(1, 30000)])
    add(coins=[1, 0, 0, 0, 0, 1], edges=[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]])
    add(
        coins=[0, 0, 0, 1, 1, 0, 0, 1],
        edges=[[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [5, 6], [5, 7]],
    )
    while len(calls) < 600:
        n = rng.randint(1, 50)
        mode = rng.randrange(4)
        edges = [
            [v, (v - 1 if mode == 0 else 0 if mode == 1 else rng.randrange(v))]
            for v in range(1, n)
        ]
        coins = [rng.randrange(2) for _ in range(n)]
        if mode == 0:
            coins = [1] + [0] * max(0, n - 2) + ([1] if n > 1 else [])
        labels = list(range(n))
        rng.shuffle(labels)
        edges = [[labels[a], labels[b]] for a, b in edges]
        relabelled = [0] * n
        for v, c in enumerate(coins):
            relabelled[labels[v]] = c
        coins = relabelled
        add(coins=coins, edges=edges)
    return calls
