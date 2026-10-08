import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    add(nums=[10000] * 1000, n=2**31 - 1)
    add(nums=[1] * 1000, n=1)
    add(nums=[1, 3], n=6)
    while len(calls) < 600:
        nums = sorted(
            rng.randint(1, 10000 if len(calls) % 4 == 0 else 30)
            for _ in range(rng.randint(1, 40))
        )
        if len(calls) % 3 == 0:
            nums = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
            n = rng.randint(1, 2047)
        else:
            n = (
                rng.randint(1, 2**31 - 1)
                if len(calls) % 4 == 0
                else rng.randint(1, 1000)
            )
        assert (
            1 <= len(nums) <= 1000
            and nums == sorted(nums)
            and all(1 <= x <= 10000 for x in nums)
            and 1 <= n <= 2**31 - 1
        )
        add(nums=nums, n=n)
    assert len(calls) == 600
    return list(calls)
