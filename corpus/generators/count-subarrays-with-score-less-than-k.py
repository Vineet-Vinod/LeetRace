import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            "candidate(nums = [2,1,4,3,5], k = 10)",
            "candidate(nums = [1,1,1], k = 5)",
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
        values(p["nums"], 1, 100000)
        assert 1 <= p["k"] <= 10**15

    add(nums=[100000] * 100000, k=10**15)
    add(nums=[1] * 100000, k=1)
    attempts = 0
    while len(calls) < 600:
        mode = attempts % 8
        attempts += 1
        n = rng.randint(1, 45)
        a = [rng.randint(1, 30) for _ in range(n)]
        if mode == 0:
            a = [rng.randint(1, 30)] * n
        k = rng.choice(
            [1, max(a), sum(a) * n, sum(a) * n + 1, rng.randint(1, sum(a) * n + 1)]
        )
        add(nums=a, k=k)
    return list(calls)
