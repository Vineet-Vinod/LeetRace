"""Seeded legal inputs, including original examples and maximum-size boundaries."""

import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def validate(kw):
        assert (
            1 <= len(kw["nums"]) <= 5000
            and all(1 <= v <= 10**9 for v in kw["nums"])
            and 0 <= kw["k"] <= min(50, len(kw["nums"]))
        )

    def add_call(call):
        kw = eval(call, {"candidate": lambda **kwargs: kwargs})
        validate(kw)
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        if key not in seen:
            seen.add(key)
            calls.append(call)

    def factory(index):
        n = rng.randint(1, 80)
        return dict(
            nums=[rng.randint(1, 8) for _ in range(n)], k=rng.randint(0, min(50, n))
        )

    for call in [
        "candidate(nums = [1,2,1,1,3], k = 2)",
        "candidate(nums = [1,2,3,4,5,1], k = 0)",
        "candidate(nums=[10**9]*5000,k=50)",
        "candidate(nums=[1,2]*2500,k=50)",
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
