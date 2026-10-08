"""Seeded legal inputs, including original examples and maximum-size boundaries."""

import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def validate(kw):
        s, a, b = kw["s"], kw["a"], kw["b"]
        assert (
            1 <= kw["k"] <= len(s) <= 500000
            and 1 <= len(a) <= 500000
            and 1 <= len(b) <= 500000
        )
        assert all(
            c in "abcdefghijklmnopqrstuvwxyz" for text in (s, a, b) for c in text
        )

    def add_call(call):
        kw = eval(call, {"candidate": lambda **kwargs: kwargs})
        validate(kw)
        key = ast.dump(ast.parse(call, mode="eval"), include_attributes=False)
        if key not in seen:
            seen.add(key)
            calls.append(call)

    def factory(index):
        n = rng.randint(1, 90)
        s = "".join(rng.choices("abc", k=n))
        if index % 3 == 0:
            a = s[rng.randrange(n) :]
            b = a
        elif index % 3 == 1:
            a = "z"
            b = "zz"
        else:
            start = rng.randrange(n)
            a = s[start : start + rng.randint(1, 8)]
            start = rng.randrange(n)
            b = s[start : start + rng.randint(1, 8)]
        return dict(s=s, a=a, b=b, k=rng.randint(1, n))

    for call in [
        'candidate(s = "isawsquirrelnearmysquirrelhouseohmy", a = "my", b = "squirrel", k = 15)',
        'candidate(s = "abcd", a = "a", b = "a", k = 4)',
        "candidate(s='a'*500000,a='a'*500000,b='a'*500000,k=500000)",
        "candidate(s='a'*500000,a='b',b='a',k=1)",
        "candidate(s='a'*500000,a='a',b='a',k=1)",
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
