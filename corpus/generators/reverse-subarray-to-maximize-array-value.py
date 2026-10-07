"""Seeded legal inputs, including original examples and maximum-size boundaries."""

import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def validate(kw):
        nums = kw["nums"]
        assert 2 <= len(nums) <= 30000 and all(-100000 <= v <= 100000 for v in nums)
        # Any reversal introduces at most two edges, each with value at most 200000.
        assert sum(abs(a - b) for a, b in zip(nums, nums[1:])) + 400000 < 2**31

    def add_call(call):
        kw = eval(call, {"candidate": lambda **kwargs: kwargs})
        validate(kw)
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        if key not in seen:
            seen.add(key)
            calls.append(call)

    def factory(index):
        n = rng.randint(2, 100)
        nums = [rng.randint(-100000, 100000) for _ in range(n)]
        if index % 4 == 0:
            nums.sort()
        if index % 4 == 1:
            nums = [rng.randint(-100000, 100000)] * n
        return dict(nums=nums)

    for call in [
        "candidate(nums = [2,3,1,5,4])",
        "candidate(nums = [2,4,9,24,2,1,10])",
        "candidate(nums=[-100000]*15000+[100000]*15000)",
        "candidate(nums=[0]*30000)",
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
