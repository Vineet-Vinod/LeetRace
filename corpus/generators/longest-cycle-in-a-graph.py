import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    add(edges=list(range(1, 100000)) + [0])
    add(edges=list(range(1, 100000)) + [-1])
    while len(calls) < 600:
        n = rng.randint(2, 60)
        if len(calls) % 3 == 0:
            edges = [
                rng.randrange(i + 1, n) if i + 1 < n and rng.random() < 0.9 else -1
                for i in range(n)
            ]
        elif len(calls) % 3 == 1:
            order = list(range(n))
            rng.shuffle(order)
            edges = [-1] * n
            for i, v in enumerate(order):
                edges[v] = order[(i + 1) % n]
        else:
            edges = [
                rng.choice([-1] + [j for j in range(n) if j != i]) for i in range(n)
            ]
        assert 2 <= n <= 100000 and all(
            -1 <= v < n and v != i for i, v in enumerate(edges)
        )
        add(edges=edges)
    assert len(calls) == 600
    return list(calls)
