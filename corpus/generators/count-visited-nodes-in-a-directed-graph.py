import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        e = d["edges"]
        assert 2 <= len(e) <= 100000 and all(
            0 <= v < len(e) and v != i for i, v in enumerate(e)
        )

    def add(**kwargs):
        valid(kwargs)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(edges=[1, 2, 0, 0])
    add(edges=[1, 2, 3, 4, 0])
    add(edges=list(range(1, 100000)) + [0])
    add(edges=[1, 0] + list(range(1, 99999)))
    t = 0
    while len(calls) < 600:
        n = rng.randint(2, 40)
        edges = []
        for i in range(n):
            v = rng.randrange(n - 1)
            edges.append(v + (v >= i))
        if t % 4 == 0:
            edges = [(i + 1) % n for i in range(n)]
        if t % 4 == 1:
            edges = [1, 0] + [rng.randrange(i) for i in range(2, n)]
        add(edges=edges)
        t += 1
    return calls
