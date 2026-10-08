import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        h, q = kw["heights"], kw["queries"]
        n = len(h)
        assert 1 <= n <= 50000 and all(1 <= v <= 10**9 for v in h)
        assert 1 <= len(q) <= 50000 and all(
            len(v) == 2 and all(0 <= x < n for x in v) for v in q
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [
        {
            "heights": [6, 4, 8, 5, 2, 7],
            "queries": [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]],
        },
        {
            "heights": [5, 3, 8, 2, 6, 1, 4, 6],
            "queries": [[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]],
        },
    ] + [
        {"heights": [10**9] * 50000, "queries": [[i, 49999 - i] for i in range(50000)]},
        {"heights": list(range(1, 50001)), "queries": [[0, 49999], [49999, 0], [1, 1]]},
    ]:
        add(**kw)
    while len(calls) < 600:
        n = rng.randint(1, 50)
        mode = len(calls) % 4
        h = [rng.randint(1, 20) for _ in range(n)]
        if mode == 0:
            h = sorted(h)
        if mode == 1:
            h = sorted(h, reverse=True)
        q = [[rng.randrange(n), rng.randrange(n)] for _ in range(rng.randint(1, 30))]
        add(heights=h, queries=q)
    return calls
