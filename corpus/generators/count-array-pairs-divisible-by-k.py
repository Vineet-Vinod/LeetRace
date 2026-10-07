"""Seeded legal inputs, including original examples and maximum-size boundaries."""

import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def validate(kw):
        assert (
            1 <= len(kw["nums"]) <= 10**5
            and 1 <= kw["k"] <= 10**5
            and all(1 <= v <= 10**5 for v in kw["nums"])
        )

    def add_call(call):
        kw = eval(call, {"candidate": lambda **kwargs: kwargs})
        validate(kw)
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        if key not in seen:
            seen.add(key)
            calls.append(call)

    def factory(index):
        k = rng.choice([1, 2, 6, 12, 30, 60, 99991, 100000, rng.randint(1, 100000)])
        n = rng.randint(1, 70)
        nums = [rng.choice([1, k, rng.randint(1, 100000)]) for _ in range(n)]
        if index % 4 == 0:
            k = 2
            nums = [2 * rng.randint(0, 49999) + 1 for _ in range(n)]
        return dict(nums=nums, k=k)

    for call in [
        "candidate(nums = [1,2,3,4,5], k = 2)",
        "candidate(nums = [1,2,3,4], k = 5)",
        "candidate(nums=[100000]*100000,k=100000)",
        "candidate(nums=[1]*100000,k=99991)",
        "candidate(nums=[1],k=1)",
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
