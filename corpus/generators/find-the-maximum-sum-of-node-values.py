import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        v, k, e = kw["nums"], kw["k"], kw["edges"]
        n = len(v)
        assert 2 <= n <= 20000 and 1 <= k <= 10**9 and all(0 <= x <= 10**9 for x in v)
        assert len(e) == n - 1 and all(
            len(edge) == 2 and 0 <= edge[0] < edge[1] < n for edge in e
        )
        # Each i>0 has exactly one lower-numbered parent, proving a connected acyclic tree.
        assert sorted(edge[1] for edge in e) == list(range(1, n))
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [
        {"nums": [1, 2, 1], "k": 3, "edges": [[0, 1], [0, 2]]},
        {"nums": [2, 3], "k": 7, "edges": [[0, 1]]},
        {
            "nums": [7, 7, 7, 7, 7, 7],
            "k": 3,
            "edges": [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]],
        },
    ] + [
        {
            "nums": [0] * 20000,
            "k": 10**9,
            "edges": [[i - 1, i] for i in range(1, 20000)],
        },
        {"nums": [10**9] * 20000, "k": 1, "edges": [[0, i] for i in range(1, 20000)]},
    ]:
        add(**kw)
    while len(calls) < 600:
        n = rng.randint(2, 50)
        k = rng.randint(1, 1023)
        v = [rng.randint(0, 2047) for _ in range(n)]
        if len(calls) % 4 == 0:
            v = [k] * n
        e = [[rng.randrange(i), i] for i in range(1, n)]
        add(nums=v, k=k, edges=e)
    return calls
