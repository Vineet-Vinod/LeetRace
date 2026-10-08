"""Seeded legal inputs, including original examples and maximum-size boundaries."""

import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def validate(kw):
        assert 1 <= len(kw["nums"]) <= 100000 and all(
            1 <= v <= 10**9 for v in kw["nums"]
        )

    def add_call(call):
        kw = eval(call, {"candidate": lambda **kwargs: kwargs})
        validate(kw)
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        if key not in seen:
            seen.add(key)
            calls.append(call)

    def factory(index):
        nums = [
            rng.randint(1, 100 if index % 2 else 10**9)
            for _ in range(rng.randint(1, 100))
        ]
        if index % 3 == 0:
            nums.sort()
        return dict(nums=nums)

    for call in [
        "candidate(nums = [3,9,3])",
        "candidate(nums = [1,2,3,4,5])",
        "candidate(nums=[10**9]*99999+[1])",
        "candidate(nums=[1]*100000)",
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
