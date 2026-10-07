import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**args) -> None:
        a, lo, hi = args["nums"], args["lower"], args["upper"]
        assert 1 <= len(a) <= 100000 and all(-(2**31) <= x <= 2**31 - 1 for x in a)
        assert -100000 <= lo <= hi <= 100000
        # The universal subarray-count bound proves the promise for modest cases.
        # The two long cases have respectively zero and len(a) qualifying sums.
        if len(a) > 65535:
            assert (all(x == 2**31 - 1 for x in a) and hi <= 100000) or (
                all(x == 1 for x in a) and lo == hi == 1
            )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in args.items())
            + ")"
        )
        calls[call] = None

    add(nums=[-2, 5, -1], lower=-2, upper=2)
    add(nums=[0], lower=0, upper=0)
    add(nums=[2**31 - 1] * 100000, lower=-100000, upper=100000)
    add(nums=[1] * 100000, lower=1, upper=1)
    add(nums=[-(2**31), 2**31 - 1], lower=-100000, upper=100000)
    add(nums=[-2, 5, -1], lower=-2, upper=2)
    while len(calls) < 600:
        n = rng.randint(1, 50)
        a = [rng.randint(-20, 20) for _ in range(n)]
        lo, hi = sorted([rng.randint(-100, 100), rng.randint(-100, 100)])
        if len(calls) % 4 == 0:
            lo = hi = rng.choice(a)
        if len(calls) % 4 == 1:
            a = [0] * n
            lo, hi = sorted([0, rng.randint(-10, 10)])
        add(nums=a, lower=lo, upper=hi)
    return list(calls)[:600]
