import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(edges: list[list[int]], cost: list[int]) -> None:
        n = len(cost)
        assert (
            2 <= n <= 20000
            and len(edges) == n - 1
            and all(1 <= abs(x) <= 10000 for x in cost)
        )
        parent = list(range(n))

        def find(x: int) -> int:
            while parent[x] != x:
                x = parent[x]
            return x

        for a, b in edges:
            assert 0 <= a < n and 0 <= b < n and find(a) != find(b)
            parent[find(a)] = find(b)
        assert len({find(x) for x in range(n)}) == 1
        call = (
            "candidate("
            + ", ".join(
                f"{key}={value!r}" for key, value in [("edges", edges), ("cost", cost)]
            )
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(edges=[[0, 1], [0, 2]], cost=[1, 2, -2])
    add(
        edges=[[i - 1, i] for i in range(1, 20000)],
        cost=[10000 if i % 2 else -10000 for i in range(20000)],
    )
    add(edges=[[0, i] for i in range(1, 20000)], cost=[-10000] * 20000)
    add(edges=[[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]], cost=[1, 2, 3, 4, 5, 6])
    add(
        edges=[[0, 1], [0, 2], [1, 3], [1, 4], [1, 5], [2, 6], [2, 7], [2, 8]],
        cost=[1, 4, 2, 3, 5, 7, 8, -4, 2],
    )
    add(edges=[[0, 1], [0, 2]], cost=[1, 2, -2])
    while len(calls) < 600:
        n = rng.randint(2, 45)
        edges = [[rng.randrange(i), i] for i in range(1, n)]
        rng.shuffle(edges)
        cost = [rng.choice([-1, 1]) * rng.randint(1, 10000) for _ in range(n)]
        if len(calls) % 4 == 0:
            cost = [-rng.randint(1, 10000) for _ in range(n)]
        add(edges=edges, cost=cost)
    return calls
