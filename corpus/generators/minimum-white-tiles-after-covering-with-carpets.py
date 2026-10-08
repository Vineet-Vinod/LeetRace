"""Seeded legal inputs, including original examples and maximum-size boundaries."""

import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def validate(kw):
        f = kw["floor"]
        assert (
            1 <= kw["carpetLen"] <= len(f) <= 1000
            and all(c in "01" for c in f)
            and 1 <= kw["numCarpets"] <= 1000
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
        floor = "".join(rng.choices("01", k=n))
        if index % 2:
            num = rng.randint(1, max(1, n // 5))
            length = rng.randint(1, max(1, n // (num + 1)))
        else:
            num = rng.randint(1, 1000)
            length = rng.randint(1, n)
        return dict(floor=floor, numCarpets=num, carpetLen=length)

    for call in [
        'candidate(floor = "10110101", numCarpets = 2, carpetLen = 2)',
        'candidate(floor = "11111", numCarpets = 2, carpetLen = 3)',
        "candidate(floor='1'*1000,numCarpets=499,carpetLen=2)",
        "candidate(floor='1'*1000,numCarpets=1000,carpetLen=1000)",
        "candidate(floor='0'*1000,numCarpets=1,carpetLen=1)",
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
