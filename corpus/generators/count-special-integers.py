"""Seeded legal inputs, including original examples and maximum-size boundaries."""

import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def validate(kw):
        assert 1 <= kw["n"] <= 2 * 10**9

    def add_call(call):
        kw = eval(call, {"candidate": lambda **kwargs: kwargs})
        validate(kw)
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        if key not in seen:
            seen.add(key)
            calls.append(call)

    def factory(index):
        return dict(
            n=rng.randint(1, 10000) if index % 2 == 0 else rng.randint(1, 2 * 10**9)
        )

    for call in [
        "candidate(n = 20)",
        "candidate(n = 5)",
        "candidate(n = 135)",
        "candidate(n=1)",
        "candidate(n=2000000000)",
        "candidate(n=987654321)",
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
