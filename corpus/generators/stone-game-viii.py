"""Seeded legal inputs, including original examples and maximum-size boundaries."""

import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def validate(kw):
        assert 2 <= len(kw["stones"]) <= 100000 and all(
            -10000 <= v <= 10000 for v in kw["stones"]
        )

    def add_call(call):
        kw = eval(call, {"candidate": lambda **kwargs: kwargs})
        validate(kw)
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        if key not in seen:
            seen.add(key)
            calls.append(call)

    def factory(index):
        if index % 4 == 0:
            return dict(stones=[-rng.randint(1, 10000), -rng.randint(1, 10000)])
        return dict(
            stones=[rng.randint(-10000, 10000) for _ in range(rng.randint(2, 100))]
        )

    for call in [
        "candidate(stones = [-1,2,-3,4,-5])",
        "candidate(stones = [7,-6,5,10,5,-2,-6])",
        "candidate(stones = [-10,-12])",
        "candidate(stones=[10000]*100000)",
        "candidate(stones=[-10000]*100000)",
        "candidate(stones=[0]*100000)",
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
