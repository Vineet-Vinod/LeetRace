"""Seeded legal inputs, including original examples and maximum-size boundaries."""

import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def validate(kw):
        n = kw["n"]
        h = kw["highways"]
        assert 2 <= n <= 15 and 1 <= kw["k"] <= 50 and 1 <= len(h) <= 50
        assert all(
            len(e) == 3
            and 0 <= e[0] < n
            and 0 <= e[1] < n
            and e[0] != e[1]
            and 0 <= e[2] <= 100
            for e in h
        )
        edges = [tuple(sorted(e[:2])) for e in h]
        assert len(edges) == len(set(edges))

    def add_call(call):
        kw = eval(call, {"candidate": lambda **kwargs: kwargs})
        validate(kw)
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        if key not in seen:
            seen.add(key)
            calls.append(call)

    def factory(index):
        n = rng.randint(2, 9)
        pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
        rng.shuffle(pairs)
        h = [
            [i, j, rng.randint(0, 100)]
            for i, j in pairs[: rng.randint(1, min(25, len(pairs)))]
        ]
        k = rng.randint(1, n - 1) if index % 3 else rng.randint(n, 50)
        return dict(n=n, highways=h, k=k)

    for call in [
        "candidate(n = 5, highways = [[0,1,4],[2,1,3],[1,4,11],[3,2,3],[3,4,2]], k = 3)",
        "candidate(n = 4, highways = [[0,1,3],[2,3,2]], k = 2)",
        "candidate(n=15,highways=[[i,i+1,100] for i in range(14)],k=14)",
        "candidate(n=15,highways=[[i,j,100] for i in range(15) for j in range(i+1,15)][:50],k=50)",
        "candidate(n=2,highways=[[0,1,0]],k=1)",
    ]:
        add_call(call)
    index = 0
    while len(calls) < 600:
        kw = factory(index)
        add_call(
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kw.items())
            + ")"
        )
        index += 1
    assert len(calls) == len(set(calls)) == 600
    return calls
