import ast
import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = dict.fromkeys(
        ast.unparse(ast.parse(call, mode="eval"))
        for call in [
            "candidate(nums1 = [3,2,5], nums2 = [2,2,1], diff = 1)",
            "candidate(nums1 = [3,-1], nums2 = [-2,2], diff = -1)",
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
        values(p["nums1"], -10000, 10000, 2)
        values(p["nums2"], -10000, 10000, 2)
        assert len(p["nums1"]) == len(p["nums2"]) and -10000 <= p["diff"] <= 10000

    add(nums1=[-10000] * 100000, nums2=[10000] * 100000, diff=10000)
    add(nums1=[10000] * 100000, nums2=[-10000] * 100000, diff=-10000)
    attempts = 0
    while len(calls) < 600:
        mode = attempts % 8
        attempts += 1
        n = rng.randint(2, 70)
        a = [rng.randint(-10000, 10000) for _ in range(n)]
        b = [rng.randint(-10000, 10000) for _ in range(n)]
        if mode == 0:
            b = a.copy()
        add(
            nums1=a,
            nums2=b,
            diff=rng.choice([-10000, 0, 10000, rng.randint(-10000, 10000)]),
        )
    return list(calls)
