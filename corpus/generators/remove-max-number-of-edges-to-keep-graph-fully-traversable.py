import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        n = d["n"]
        e = d["edges"]
        assert (
            1 <= n <= 100000
            and 1 <= len(e) <= min(100000, 3 * n * (n - 1) // 2)
            and len({tuple(p) for p in e}) == len(e)
        )
        assert all(len(p) == 3 and 1 <= p[0] <= 3 and 1 <= p[1] < p[2] <= n for p in e)

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

    add(n=4, edges=[[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]])
    add(n=4, edges=[[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]])
    add(n=4, edges=[[3, 2, 3], [1, 1, 2], [2, 3, 4]])
    add(n=100000, edges=[[3, i, i + 1] for i in range(1, 100000)] + [[1, 1, 100000]])
    add(n=100000, edges=[[1, i, i + 1] for i in range(1, 100000)])
    t = 0
    while len(calls) < 600:
        n = rng.randint(2, 20)
        pairs = [(u, v) for u in range(1, n + 1) for v in range(u + 1, n + 1)]
        e = set()
        if t % 3:
            for v in range(2, n + 1):
                u = rng.randrange(1, v)
                if t % 3 == 1:
                    e.add((3, u, v))
                else:
                    e.update(((1, u, v), (2, u, v)))
        for _ in range(rng.randint(1, 60)):
            u, v = rng.choice(pairs)
            e.add((rng.randint(1, 3), u, v))
        add(n=n, edges=[list(p) for p in sorted(e)])
        t += 1
    return calls
