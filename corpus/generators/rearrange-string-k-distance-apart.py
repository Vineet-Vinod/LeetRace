import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            'candidate(s = "aabbcc", k = 3)',
            'candidate(s = "aaabc", k = 3)',
            'candidate(s = "aaadbbcc", k = 2)',
        ]
    )

    def add(**kwargs):
        validate(kwargs)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        calls[ast.unparse(ast.parse(call, mode="eval"))] = None

    def validate(p):
        assert 1 <= len(p["s"]) <= 300000 and all("a" <= x <= "z" for x in p["s"])
        assert 0 <= p["k"] <= len(p["s"])

    add(s="abc" * 100000, k=3)
    add(s="a" * 300000, k=300000)
    add(s="z" * 300000, k=0)
    attempts = 0
    while len(calls) < 600:
        mode = attempts % 8
        attempts += 1
        n = rng.randint(1, 90)
        s = "".join(rng.choice("abcdef") for _ in range(n))
        k = rng.randint(0, min(n, 10))
        if mode < 3:
            letters = rng.sample("abcdefghijklmnopqrstuvwxyz", rng.randint(1, 12))
            s = "".join(letters) * rng.randint(1, 10)
            k = rng.randint(0, len(letters))
        if mode == 3:
            k = len(s)
        add(s=s, k=k)
    return list(calls)
