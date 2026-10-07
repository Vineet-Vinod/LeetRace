import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            "candidate(nums = [1,4,3,3,2], andValues = [0,3,3,2])",
            "candidate(nums = [2,3,5,7,7,7,5], andValues = [0,7,5])",
            "candidate(nums = [1,2,3,4], andValues = [2])",
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
        values(p["nums"], 1, 99999, 1, 10000)
        values(p["andValues"], 0, 99999, 1, min(len(p["nums"]), 10))

    add(nums=[99999] * 10000, andValues=[99999] * 10)
    add(nums=[1, 2] * 5000, andValues=[0] * 10)
    attempts = 0
    while len(calls) < 600:
        mode = attempts % 8
        attempts += 1
        n = rng.randint(1, 35)
        m = rng.randint(1, min(n, 10))
        a = [rng.randint(1, 63 if mode < 6 else 99999) for _ in range(n)]
        if mode < 5:
            cuts = [0] + sorted(rng.sample(range(1, n), m - 1)) + [n]
            targets = []
            for left, right in zip(cuts, cuts[1:]):
                mask = a[left]
                for x in a[left + 1 : right]:
                    mask &= x
                targets.append(mask)
        else:
            targets = [rng.randint(0, 63) for _ in range(m)]
        add(nums=a, andValues=targets)
    return list(calls)
