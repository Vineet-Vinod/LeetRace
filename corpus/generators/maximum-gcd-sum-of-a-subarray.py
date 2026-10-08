import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    add(nums=[1000000] * 100000, k=100000)
    add(nums=[1] * 100000, k=1)
    while len(calls) < 600:
        n = rng.randint(1, 45)
        factor = rng.choice((1, 2, 6, 1000))
        nums = [factor * rng.randint(1, 1000) for _ in range(n)]
        k = rng.randint(1, n)
        assert 1 <= n <= 100000 and 1 <= k <= n and all(1 <= x <= 1000000 for x in nums)
        add(nums=nums, k=k)
    assert len(calls) == 600
    return list(calls)
