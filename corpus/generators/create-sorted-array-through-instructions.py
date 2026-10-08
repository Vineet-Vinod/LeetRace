import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            "candidate(instructions = [1,5,6,2])",
            "candidate(instructions = [1,2,3,6,5,4])",
            "candidate(instructions = [1,3,3,3,2,4,2,1,2])",
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
        values(p["instructions"], 1, 100000)

    add(instructions=list(range(1, 100001)))
    add(instructions=[1, 100000] * 50000)
    attempts = 0
    while len(calls) < 600:
        mode = attempts % 8
        attempts += 1
        n = rng.randint(1, 70)
        a = [rng.randint(1, 20 if mode < 4 else 100000) for _ in range(n)]
        if mode == 0:
            a.sort()
        if mode == 1:
            a.sort(reverse=True)
        add(instructions=a)
    return list(calls)
