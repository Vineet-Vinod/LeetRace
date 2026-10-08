"""Seeded legal inputs, including original examples and maximum-size boundaries."""

import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def validate(kw):
        n = len(kw["nums1"])
        assert 1 <= n <= 100000 and len(kw["nums2"]) == n
        assert all(v in (0, 1) for v in kw["nums1"]) and all(
            0 <= v <= 10**9 for v in kw["nums2"]
        )
        assert 1 <= len(kw["queries"]) <= 100000
        for kind, a, b in kw["queries"]:
            assert kind in (1, 2, 3)
            assert (
                (0 <= a <= b < n)
                if kind == 1
                else (0 <= a <= 10**6 and b == 0)
                if kind == 2
                else (a == b == 0)
            )

    def add_call(call):
        kw = eval(call, {"candidate": lambda **kwargs: kwargs})
        validate(kw)
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        if key not in seen:
            seen.add(key)
            calls.append(call)

    def factory(index):
        n = rng.randint(1, 60)
        queries = []
        for _ in range(rng.randint(1, 60)):
            kind = rng.randint(1, 3)
            if kind == 1:
                a = rng.randrange(n)
                queries.append([1, a, rng.randint(a, n - 1)])
            elif kind == 2:
                queries.append(
                    [2, rng.choice([0, 1, 1000000, rng.randint(1, 1000)]), 0]
                )
            else:
                queries.append([3, 0, 0])
        return dict(
            nums1=[rng.randint(0, 1) for _ in range(n)],
            nums2=[rng.randint(0, 1000) for _ in range(n)],
            queries=queries,
        )

    for call in [
        "candidate(nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]])",
        "candidate(nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]])",
        "candidate(nums1=[1]*100000,nums2=[10**9]*100000,queries=[[1,0,99999],[2,1000000,0],[3,0,0]])",
        "candidate(nums1=[0],nums2=[0],queries=[[1,0,0],[2,1000000,0],[3,0,0]]*33333+[[3,0,0]])",
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
