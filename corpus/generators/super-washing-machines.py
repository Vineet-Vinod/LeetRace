import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            "candidate(machines = [1,0,5])",
            "candidate(machines = [0,3,0])",
            "candidate(machines = [0,2,0])",
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
        values(p["machines"], 0, 100000, 1, 10000)

    add(machines=[100000] * 10000)
    add(machines=[100000] + [0] * 9999)
    attempts = 0
    while len(calls) < 600:
        mode = attempts % 8
        attempts += 1
        n = rng.randint(1, 40)
        a = [rng.randint(0, 1000) for _ in range(n)]
        if mode < 5:
            a[-1] += (-sum(a)) % n
        if mode == 0:
            a = [rng.randint(0, 100000)] * n
        add(machines=a)
    return list(calls)
