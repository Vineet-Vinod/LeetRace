import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            "candidate(nums = [1,4,3,3,2])",
            "candidate(nums = [3,3,3])",
            "candidate(nums = [1])",
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
        values(p["nums"], 1, 10**9)

    add(nums=[10**9] * 100000)
    add(nums=list(range(1, 100001)))
    attempts = 0
    while len(calls) < 600:
        mode = attempts % 8
        attempts += 1
        n = rng.randint(1, 70)
        a = [rng.randint(1, 10 if mode < 4 else 10**9) for _ in range(n)]
        if mode == 0:
            a = [rng.randint(1, 100)] * n
        if mode == 1:
            a.sort()
        add(nums=a)
    return list(calls)
