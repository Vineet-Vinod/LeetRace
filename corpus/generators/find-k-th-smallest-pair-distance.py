import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            "candidate(nums = [1,3,1], k = 1)",
            "candidate(nums = [1,1,1], k = 2)",
            "candidate(nums = [1,6,1], k = 3)",
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
        values(p["nums"], 0, 10**6, 2, 10000)
        assert 1 <= p["k"] <= len(p["nums"]) * (len(p["nums"]) - 1) // 2

    add(nums=[0, 10**6] * 5000, k=49995000)
    add(nums=[0] * 10000, k=1)
    attempts = 0
    while len(calls) < 600:
        mode = attempts % 8
        attempts += 1
        n = rng.randint(2, 45)
        a = [rng.randint(0, 8 if mode < 4 else 10**6) for _ in range(n)]
        k = rng.choice([1, n * (n - 1) // 2, rng.randint(1, n * (n - 1) // 2)])
        add(nums=a, k=k)
    return list(calls)
