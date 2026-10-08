import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            "candidate(favorite = [2,2,1,2])",
            "candidate(favorite = [1,2,0])",
            "candidate(favorite = [3,0,1,4,1])",
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
        n = len(p["favorite"])
        values(p["favorite"], 0, n - 1, 2)
        assert all(i != v for i, v in enumerate(p["favorite"]))

    add(favorite=list(range(1, 100000)) + [0])
    add(favorite=[i ^ 1 for i in range(100000)])
    attempts = 0
    while len(calls) < 600:
        mode = attempts % 8
        attempts += 1
        n = rng.randint(2, 70)
        f = [rng.randrange(n - 1) for _ in range(n)]
        f = [v + (v >= i) for i, v in enumerate(f)]
        if mode == 0:
            f = list(range(1, n)) + [0]
        if mode == 1:
            f = [1, 0] + [rng.randrange(i) for i in range(2, n)]
        add(favorite=f)
    return list(calls)
