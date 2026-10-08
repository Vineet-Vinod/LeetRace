import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(n, edges, query):
        assert 2 <= n <= 100000 and 0 <= len(edges) <= 100000
        assert all(
            len(e) == 3
            and 0 <= e[0] < n
            and 0 <= e[1] < n
            and e[0] != e[1]
            and 0 <= e[2] <= 100000
            for e in edges
        )
        assert 1 <= len(query) <= 100000
        assert all(
            len(q) == 2 and 0 <= q[0] < n and 0 <= q[1] < n and q[0] != q[1]
            for q in query
        )
        call = (
            "candidate("
            + ", ".join(
                f"{name}={value!r}"
                for name, value in (
                    ("n", n),
                    ("edges", edges),
                    ("query", query),
                )
            )
            + ")"
        )
        calls[call] = None

    add(n=5, edges=[[0, 1, 7], [1, 3, 7], [1, 2, 1]], query=[[0, 3], [3, 4]])
    add(n=3, edges=[[0, 2, 7], [0, 1, 15], [1, 2, 6], [1, 2, 1]], query=[[1, 2]])
    add(
        n=100000,
        edges=[[i, i + 1, 100000] for i in range(99999)] + [[0, 1, 0]],
        query=[[0, i] for i in range(1, 100000)] + [[99998, 99999]],
    )
    add(n=100000, edges=[], query=[[0, 99999]])
    while len(calls) < 600:
        n = rng.randint(2, 30)
        mode = rng.randrange(4)
        if mode == 0:
            edges = [[i - 1, i, rng.choice((7, 15, 31, 100000))] for i in range(1, n)]
        elif mode == 1:
            edges = []
        elif mode == 2:
            split = max(1, n // 2)
            edges = [[i - 1, i, rng.randint(0, 31)] for i in range(1, n) if i != split]
        else:
            edges = [
                rng.sample(range(n), 2) + [rng.randint(0, 100000)]
                for _ in range(rng.randint(1, 2 * n))
            ]
        query = [rng.sample(range(n), 2) for _ in range(rng.randint(1, 25))]
        add(n=n, edges=edges, query=query)
    return list(calls)
