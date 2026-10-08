"""Seeded legal inputs, including original examples and maximum-size boundaries."""

import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def validate(kw):
        assert 1 <= len(kw["courses"]) <= 10000 and all(
            len(c) == 2 and all(1 <= v <= 10000 for v in c) for c in kw["courses"]
        )

    def add_call(call):
        kw = eval(call, {"candidate": lambda **kwargs: kwargs})
        validate(kw)
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        if key not in seen:
            seen.add(key)
            calls.append(call)

    def factory(index):
        n = rng.randint(1, 15)
        mode = index % 4
        courses = [[rng.randint(1, 20), rng.randint(1, 100)] for _ in range(n)]
        if mode == 0:
            courses = [[rng.randint(2, 100), 1] for _ in range(n)]
        if mode == 1:
            courses = [[rng.randint(1, 10), 1000] for _ in range(n)]
        return dict(courses=courses)

    for call in [
        "candidate(courses = [[100,200],[200,1300],[1000,1250],[2000,3200]])",
        "candidate(courses = [[1,2]])",
        "candidate(courses = [[3,2],[4,3]])",
        "candidate(courses=[[1,10000]]*10000)",
        "candidate(courses=[[10000,1]]*10000)",
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
