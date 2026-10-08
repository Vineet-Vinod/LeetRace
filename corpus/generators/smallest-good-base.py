"""Seeded legal inputs, including original examples and maximum-size boundaries."""

import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def validate(kw):
        n = kw["n"]
        assert n.isdecimal() and n[0] != "0" and 3 <= int(n) <= 10**18

    def add_call(call):
        kw = eval(call, {"candidate": lambda **kwargs: kwargs})
        validate(kw)
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        if key not in seen:
            seen.add(key)
            calls.append(call)

    def factory(index):
        if index % 2 == 0:
            base = rng.randint(2, 1000)
            length = rng.randint(3, 7)
            value = sum(base**j for j in range(length))
            if value > 10**18:
                value = base * base + base + 1
        else:
            value = rng.randint(3, 10**18)
        return dict(n=str(value))

    for call in [
        'candidate(n = "13")',
        'candidate(n = "4681")',
        'candidate(n = "1000000000000000000")',
        "candidate(n='1000000000000000000')",
        "candidate(n='3')",
        "candidate(n='576460752303423487')",
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
