import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            "candidate(nums = [1,2,3,4,5])",
            "candidate(nums = [10,100])",
            "candidate(nums = [500,520,2500,3000])",
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
        values(p["nums"], 1, 2**20 - 1, 1, 50000)

    add(nums=[2**20 - 1] * 50000)
    add(nums=list(range(1, 50001)))
    attempts = 0
    while len(calls) < 600:
        mode = attempts % 8
        attempts += 1
        n = rng.randint(1, 55)
        a = [rng.randint(1, 2**20 - 1 if mode < 4 else 100) for _ in range(n)]
        if mode == 0:
            a = [rng.randint(1, 2**20 - 1)] * n
        if mode == 1:
            a = [1 << i for i in rng.sample(range(20), min(n, 20))]
        add(nums=a)
    return list(calls)
