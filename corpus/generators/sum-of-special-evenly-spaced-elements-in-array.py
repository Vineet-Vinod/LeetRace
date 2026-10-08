"""Seeded legal inputs, including original examples and maximum-size boundaries."""

import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def validate(kw):
        n = len(kw["nums"])
        assert (
            1 <= n <= 50000
            and all(0 <= v <= 10**9 for v in kw["nums"])
            and 1 <= len(kw["queries"]) <= 150000
        )
        assert all(
            len(q) == 2 and 0 <= q[0] < n and 1 <= q[1] <= 50000 for q in kw["queries"]
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
        nums = [rng.randint(0, 10**9) for _ in range(n)]
        queries = [
            [rng.randrange(n), rng.choice([1, 2, 50000, rng.randint(1, n)])]
            for _ in range(rng.randint(1, 60))
        ]
        return dict(nums=nums, queries=queries)

    for call in [
        "candidate(nums = [0,1,2,3,4,5,6,7], queries = [[0,3],[5,1],[4,2]])",
        "candidate(nums = [100,200,101,201,102,202,10^3,203], queries = [[0,7]])",
        "candidate(nums=[10**9]*50000,queries=[[0,1],[49999,50000],[0,50000]])",
        "candidate(nums=[10**9],queries=[[0,1]]*150000)",
        "candidate(nums=[0]*50000,queries=[[i%50000,1+i%223] for i in range(150000)])",
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
