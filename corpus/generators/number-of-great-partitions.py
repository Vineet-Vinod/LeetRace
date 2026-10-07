"""Seeded legal inputs, including original examples and maximum-size boundaries."""

import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def validate(kw):
        assert (
            1 <= len(kw["nums"]) <= 1000
            and 1 <= kw["k"] <= 1000
            and all(1 <= v <= 10**9 for v in kw["nums"])
        )

    def add_call(call):
        kw = eval(call, {"candidate": lambda **kwargs: kwargs})
        validate(kw)
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        if key not in seen:
            seen.add(key)
            calls.append(call)

    def factory(index):
        n = rng.randint(1, 40)
        nums = [rng.randint(1, 30) for _ in range(n)]
        k = (
            rng.randint(1, min(1000, max(1, sum(nums) // 3)))
            if index % 2
            else rng.randint(1, 1000)
        )
        return dict(nums=nums, k=k)

    for call in [
        "candidate(nums = [1,2,3,4], k = 4)",
        "candidate(nums = [3,3,3], k = 4)",
        "candidate(nums = [6,6], k = 2)",
        "candidate(nums=[1]*1000,k=1000)",
        "candidate(nums=[10**9]*1000,k=1000)",
        "candidate(nums=[1]*1000,k=500)",
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
