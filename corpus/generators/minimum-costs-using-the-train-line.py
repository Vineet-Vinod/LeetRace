"""Seeded legal inputs, including original examples and maximum-size boundaries."""

import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def validate(kw):
        n = len(kw["regular"])
        assert (
            1 <= n <= 100000
            and len(kw["express"]) == n
            and 1 <= kw["expressCost"] <= 100000
        )
        assert all(1 <= v <= 100000 for v in kw["regular"] + kw["express"])

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
            regular=[rng.randint(1, 100) for _ in range(n)],
            express=[rng.randint(1, 100) for _ in range(n)],
            expressCost=rng.randint(1, 100),
        )

    for call in [
        "candidate(regular = [1,6,9,5], express = [5,2,3,10], expressCost = 8)",
        "candidate(regular = [11,5,13], express = [7,10,6], expressCost = 3)",
        "candidate(regular=[100000]*100000,express=[1]*100000,expressCost=100000)",
        "candidate(regular=[1]*100000,express=[100000]*100000,expressCost=1)",
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
