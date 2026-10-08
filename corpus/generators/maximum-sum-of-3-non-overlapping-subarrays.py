import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    add(nums=[65535] * 20000, k=6666)
    add(nums=[1] * 20000, k=1)
    while len(calls) < 600:
        n = rng.randint(3, 50)
        nums = [rng.randint(1, 10 if len(calls) % 3 else 65535) for _ in range(n)]
        if len(calls) % 4 == 0:
            nums = [rng.randint(1, 65535)] * n
        k = rng.randint(1, n // 3)
        assert (
            1 <= k <= n // 3 and 3 <= n <= 20000 and all(1 <= x < 2**16 for x in nums)
        )
        add(nums=nums, k=k)
    assert len(calls) == 600
    return list(calls)
