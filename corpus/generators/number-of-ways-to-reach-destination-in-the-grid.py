"""Seeded legal inputs, including original examples and maximum-size boundaries."""

import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def validate(kw):
        n, m = kw["n"], kw["m"]
        assert 2 <= n <= 10**9 and 2 <= m <= 10**9 and 1 <= kw["k"] <= 100000
        assert all(
            len(kw[key]) == 2 and 1 <= kw[key][0] <= n and 1 <= kw[key][1] <= m
            for key in ("source", "dest")
        )

    def add_call(call):
        kw = eval(call, {"candidate": lambda **kwargs: kwargs})
        validate(kw)
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        if key not in seen:
            seen.add(key)
            calls.append(call)

    def factory(index):
        n, m = rng.randint(2, 1000), rng.randint(2, 1000)
        source = [rng.randint(1, n), rng.randint(1, m)]
        dest = [
            source[0] if index % 4 in (0, 1) else rng.randint(1, n),
            source[1] if index % 4 in (0, 2) else rng.randint(1, m),
        ]
        steps = rng.randint(1, 60)
        if index % 4 == 3:
            source, dest, steps = [1, 1], [n, m], 1
        return dict(n=n, m=m, k=steps, source=source, dest=dest)

    for call in [
        "candidate(n = 3, m = 2, k = 2, source = [1,1], dest = [2,2])",
        "candidate(n = 3, m = 4, k = 3, source = [1,2], dest = [2,3])",
        "candidate(n=1000000000,m=1000000000,k=100000,source=[1,1],dest=[1000000000,1000000000])",
        "candidate(n=2,m=2,k=100000,source=[1,1],dest=[1,2])",
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
