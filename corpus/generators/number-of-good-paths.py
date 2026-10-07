import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(vals, edges):
        n = len(vals)
        assert 1 <= n <= 30000 and all(0 <= v <= 100000 for v in vals)
        assert len(edges) == n - 1
        assert all(
            len(e) == 2 and 0 <= e[0] < n and 0 <= e[1] < n and e[0] != e[1]
            for e in edges
        )
        # Each generated edge attaches a new numbered vertex to an earlier one: connected and acyclic.
        assert sorted(max(e) for e in edges) == list(range(1, n))
        assert all(min(e) < max(e) for e in edges)
        call = (
            "candidate("
            + ", ".join(
                f"{name}={value!r}"
                for name, value in (
                    ("vals", vals),
                    ("edges", edges),
                )
            )
            + ")"
        )
        calls[call] = None

    add(vals=[1, 3, 2, 1, 3], edges=[[0, 1], [0, 2], [2, 3], [2, 4]])
    add(vals=[1, 1, 2, 2, 3], edges=[[0, 1], [1, 2], [2, 3], [2, 4]])
    add(vals=[1], edges=[])
    add(vals=[100000] * 30000, edges=[[i - 1, i] for i in range(1, 30000)])
    add(vals=[0] * 30000, edges=[[0, i] for i in range(1, 30000)])
    while len(calls) < 600:
        n = rng.randint(1, 45)
        mode = rng.randrange(4)
        if mode == 0:
            vals = [rng.randint(0, 100000)] * n
        elif mode == 1:
            vals = list(range(n))
        else:
            vals = [rng.randint(0, 7) for _ in range(n)]
        if mode == 2:
            edges = [[0, i] for i in range(1, n)]
        elif mode == 3:
            edges = [[i - 1, i] for i in range(1, n)]
        else:
            edges = [[rng.randrange(i), i] for i in range(1, n)]
        add(vals=vals, edges=edges)
    return list(calls)
