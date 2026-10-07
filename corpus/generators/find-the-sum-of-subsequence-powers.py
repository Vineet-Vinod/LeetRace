import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    add(nums=[-100000000, 100000000] * 25, k=25)
    add(nums=[-100000000 + 4000000 * i for i in range(50)], k=2)
    for nums, k in [([1, 2, 3, 4], 3), ([2, 2], 2), ([4, 3, -1], 2)]:
        add(nums=nums, k=k)
    while len(calls) < 600:
        n = rng.randint(2, 14)
        nums = [rng.randint(-30, 30) for _ in range(n)]
        k = rng.randint(2, n)
        assert (
            2 <= n <= 50 and 2 <= k <= n and all(-(10**8) <= x <= 10**8 for x in nums)
        )
        add(nums=nums, k=k)
    assert len(calls) == 600
    return list(calls)
