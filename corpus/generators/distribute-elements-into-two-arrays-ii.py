"""Seeded legal inputs, including original examples and maximum-size boundaries."""

import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def validate(kw):
        assert 3 <= len(kw["nums"]) <= 100000 and all(
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
        n = rng.randint(3, 100)
        nums = [rng.randint(1, 10 if index % 2 else 10**9) for _ in range(n)]
        if index % 5 == 0:
            nums.sort(reverse=True)
        return dict(nums=nums)

    for call in [
        "candidate(nums = [2,1,3,3])",
        "candidate(nums = [5,14,3,1,2])",
        "candidate(nums = [3,3,3,3])",
        "candidate(nums=[10**9]*100000)",
        "candidate(nums=list(range(1,100001)))",
        "candidate(nums=list(range(100000,0,-1)))",
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
