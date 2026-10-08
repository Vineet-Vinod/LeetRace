import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            "candidate(jobDifficulty = [6,5,4,3,2,1], d = 2)",
            "candidate(jobDifficulty = [9,9,9], d = 4)",
            "candidate(jobDifficulty = [1,1,1], d = 3)",
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
        values(p["jobDifficulty"], 0, 1000, 1, 300)
        assert 1 <= p["d"] <= 10

    add(jobDifficulty=[1000] * 300, d=10)
    add(jobDifficulty=[0] * 300, d=1)
    attempts = 0
    while len(calls) < 600:
        mode = attempts % 8
        attempts += 1
        n = rng.randint(1, 35)
        a = [rng.randint(0, 1000) for _ in range(n)]
        if mode == 0:
            a.sort()
        if mode == 1:
            a.sort(reverse=True)
        if mode == 2:
            a = [rng.randint(0, 1000)] * n
        add(jobDifficulty=a, d=rng.randint(1, 10))
    return list(calls)
