"""Seeded legal inputs, including original examples and maximum-size boundaries."""

import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def validate(kw):
        n = len(kw["nums"])
        q = kw["removeQueries"]
        assert (
            1 <= n <= 100000
            and all(1 <= v <= 10**9 for v in kw["nums"])
            and len(q) == n
            and sorted(q) == list(range(n))
        )

    def add_call(call):
        kw = eval(call, {"candidate": lambda **kwargs: kwargs})
        validate(kw)
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        if key not in seen:
            seen.add(key)
            calls.append(call)

    def factory(index):
        n = rng.randint(1, 100)
        q = list(range(n))
        if index % 3 == 0:
            rng.shuffle(q)
        elif index % 3 == 1:
            q.reverse()
        return dict(nums=[rng.randint(1, 1000) for _ in range(n)], removeQueries=q)

    for call in [
        "candidate(nums = [1,2,5,6,1], removeQueries = [0,3,2,4,1])",
        "candidate(nums = [3,2,11,1], removeQueries = [3,2,1,0])",
        "candidate(nums=[10**9]*100000,removeQueries=list(range(100000)))",
        "candidate(nums=[1]*100000,removeQueries=list(range(99999,-1,-1)))",
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
