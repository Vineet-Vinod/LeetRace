import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = []
    seen = set()

    def add(**kw):
        n, e = kw["n"], kw["edges"]
        assert 2 <= n <= 400 and 1 <= len(e) <= n * (n - 1) // 2
        assert all(len(edge) == 2 and 1 <= min(edge) < max(edge) <= n for edge in e)
        assert len({tuple(sorted(edge)) for edge in e}) == len(e)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for kw in [
        {"n": 6, "edges": [[1, 2], [1, 3], [3, 2], [4, 1], [5, 2], [3, 6]]},
        {
            "n": 7,
            "edges": [[1, 3], [4, 1], [4, 3], [2, 5], [5, 6], [6, 7], [7, 5], [2, 6]],
        },
    ] + [
        {"n": 400, "edges": [[i, j] for i in range(1, 401) for j in range(i + 1, 401)]},
        {"n": 2, "edges": [[1, 2]]},
        {"n": 400, "edges": [[i, i + 1] for i in range(1, 400)]},
    ]:
        add(**kw)
    while len(calls) < 600:
        n = rng.randint(3, 24)
        mode = len(calls) % 3
        if mode == 0:
            e = [[1, 2], [1, 3], [2, 3]]
            e += [
                [i, j]
                for i in range(4, n + 1)
                for j in range(i + 1, n + 1)
                if rng.random() < 0.2
            ]
        elif mode == 1:
            split = n // 2
            e = [
                [i, j]
                for i in range(1, split + 1)
                for j in range(split + 1, n + 1)
                if rng.random() < 0.2
            ]
        else:
            e = [
                [i, j]
                for i in range(1, n + 1)
                for j in range(i + 1, n + 1)
                if rng.random() < 0.35
            ]
        if not e:
            e = [[1, 2]]
        add(n=n, edges=e)
    return calls
