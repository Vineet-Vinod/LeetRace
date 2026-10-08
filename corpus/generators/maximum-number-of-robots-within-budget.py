import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            "candidate(chargeTimes = [3,6,1,3,4], runningCosts = [2,1,3,4,5], budget = 25)",
            "candidate(chargeTimes = [11,12,19], runningCosts = [10,8,7], budget = 19)",
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
        values(p["chargeTimes"], 1, 100000, 1, 50000)
        values(p["runningCosts"], 1, 100000, 1, 50000)
        assert (
            len(p["chargeTimes"]) == len(p["runningCosts"])
            and 1 <= p["budget"] <= 10**15
        )

    add(chargeTimes=[100000] * 50000, runningCosts=[100000] * 50000, budget=10**15)
    add(chargeTimes=[1] * 50000, runningCosts=[1] * 50000, budget=1)
    attempts = 0
    while len(calls) < 600:
        mode = attempts % 8
        attempts += 1
        n = rng.randint(1, 70)
        a = [rng.randint(1, 100) for _ in range(n)]
        b = [rng.randint(1, 100) for _ in range(n)]
        size = rng.randint(1, n)
        budget = max(a[:size]) + size * sum(b[:size]) + rng.choice([-1, 0, 1])
        if mode == 0:
            budget = 1
        if mode == 1:
            budget = max(a) + n * sum(b)
        add(chargeTimes=a, runningCosts=b, budget=budget)
    return list(calls)
