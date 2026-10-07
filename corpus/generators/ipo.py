import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            "candidate(k = 2, w = 0, profits = [1,2,3], capital = [0,1,1])",
            "candidate(k = 3, w = 0, profits = [1,2,3], capital = [0,1,2])",
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

    def values(a, lo, hi, minimum=1, maximum=100000):
        assert minimum <= len(a) <= maximum and all(lo <= x <= hi for x in a)

    def validate(p):
        assert 1 <= p["k"] <= 100000 and 0 <= p["w"] <= 10**9
        values(p["profits"], 0, 10000)
        values(p["capital"], 0, 10**9)
        assert (
            len(p["profits"]) == len(p["capital"])
            and p["w"] + sum(p["profits"]) <= 2**31 - 1
        )

    add(k=100000, w=10**9, profits=[10000] * 100000, capital=[10**9] * 100000)
    add(k=1, w=0, profits=[0], capital=[10**9])
    attempts = 0
    while len(calls) < 600:
        mode = attempts % 8
        attempts += 1
        n = rng.randint(1, 35)
        w = rng.randint(0, 30)
        profits = [rng.randint(0, 30) for _ in range(n)]
        capital = [rng.randint(0, 100 if mode < 4 else 20) for _ in range(n)]
        add(k=rng.randint(1, n + 5), w=w, profits=profits, capital=capital)
    return list(calls)
