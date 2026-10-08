import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def valid(d):
        nums = d["nums"]
        assert 1 <= len(nums) <= 1000 and all(-(2**31) <= x < 2**31 for x in nums)
        # Small inputs have fewer than 2^20 total subsequences. The sole large family has no three-term AP.
        assert len(nums) <= 20 or nums == [
            sum(((i >> bit) & 1) * 3**bit for bit in range(10)) for i in range(1000)
        ]

    def add(**kwargs):
        valid(kwargs)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(nums=[2, 4, 6, 8, 10])
    add(nums=[7, 7, 7, 7, 7])
    add(nums=[sum(((i >> bit) & 1) * 3**bit for bit in range(10)) for i in range(1000)])
    add(nums=[-(2**31), 0, 2**31 - 1])
    add(nums=[0] * 20)
    t = 0
    while len(calls) < 600:
        n = rng.randint(1, 20)
        nums = (
            [rng.randint(-10, 10) for _ in range(n)]
            if t % 3
            else [rng.randint(-(2**31), 2**31 - 1) for _ in range(n)]
        )
        if t % 5 == 0:
            start, step = rng.randint(-30, 30), rng.randint(-5, 5)
            nums = [start + step * i for i in range(n)]
        add(nums=nums)
        t += 1
    return calls
