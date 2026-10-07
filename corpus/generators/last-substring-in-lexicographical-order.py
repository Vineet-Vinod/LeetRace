"""Seeded legal inputs, including original examples and maximum-size boundaries."""

import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def validate(kw):
        assert 1 <= len(kw["s"]) <= 400000 and all("a" <= c <= "z" for c in kw["s"])

    def add_call(call):
        kw = eval(call, {"candidate": lambda **kwargs: kwargs})
        validate(kw)
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        if key not in seen:
            seen.add(key)
            calls.append(call)

    def factory(index):
        n = rng.randint(1, 150)
        s = "".join(rng.choices("abcxyz" if index % 2 else "ab", k=n))
        return dict(s=s)

    for call in [
        'candidate(s = "abab")',
        'candidate(s = "leetcode")',
        "candidate(s='a'*400000)",
        "candidate(s='ab'*200000)",
        "candidate(s='a'*399999+'z')",
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
