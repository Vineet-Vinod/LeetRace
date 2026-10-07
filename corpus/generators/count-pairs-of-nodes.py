import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        n = d["n"]
        e = d["edges"]
        q = d["queries"]
        assert 2 <= n <= 20000 and 1 <= len(e) <= 100000 and 1 <= len(q) <= 20
        assert all(
            len(pair) == 2
            and 1 <= pair[0] <= n
            and 1 <= pair[1] <= n
            and pair[0] != pair[1]
            for pair in e
        )
        assert all(0 <= x < len(e) for x in q)

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

    add(n=4, edges=[[1, 2], [2, 4], [1, 3], [2, 3], [2, 1]], queries=[2, 3])
    add(
        n=5,
        edges=[[1, 5], [1, 5], [3, 4], [2, 5], [1, 3], [5, 1], [2, 3], [2, 5]],
        queries=[1, 2, 3, 4, 5],
    )
    add(n=20000, edges=[[1, 2]] * 100000, queries=[0, 99998, 99999])
    t = 0
    while len(calls) < 600:
        n = rng.randint(2, 25)
        length = rng.randint(1, 80)
        edges = []
        for _ in range(length):
            u, v = rng.sample(range(1, n + 1), 2)
            edges.append([u, v])
        queries = [rng.randrange(length) for _ in range(rng.randint(1, 20))]
        add(n=n, edges=edges, queries=queries)
        t += 1
    return calls
