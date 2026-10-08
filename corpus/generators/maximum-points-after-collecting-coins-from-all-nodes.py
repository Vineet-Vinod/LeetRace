import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        edges, coins, k = kwargs["edges"], kwargs["coins"], kwargs["k"]
        n = len(coins)
        assert (
            2 <= n <= 100000
            and len(edges) == n - 1
            and all(0 <= a < n and 0 <= b < n and a != b for a, b in edges)
        )
        assert all(0 <= c <= 10000 for c in coins) and 0 <= k <= 10000
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

    add(edges=[[v, v - 1] for v in range(1, 100000)], coins=[10000] * 100000, k=10000)
    add(edges=[[v, 0] for v in range(1, 100000)], coins=[0] * 100000, k=0)
    add(edges=[[0, 1], [1, 2], [2, 3]], coins=[10, 10, 3, 3], k=5)
    add(edges=[[0, 1], [0, 2]], coins=[8, 4, 4], k=0)
    while len(calls) < 600:
        n = rng.randint(2, 40)
        edges = [
            [v, (v - 1 if len(calls) % 3 == 0 else rng.randrange(v))]
            for v in range(1, n)
        ]
        coins = [rng.randint(0, 10000) for _ in range(n)]
        k = rng.choice([0, 10000, rng.randint(1, 10000)])
        labels = list(range(n))
        rng.shuffle(labels)
        edges = [[labels[a], labels[b]] for a, b in edges]
        relabelled = [0] * n
        for v, c in enumerate(coins):
            relabelled[labels[v]] = c
        coins = relabelled
        add(edges=edges, coins=coins, k=k)
    return calls
