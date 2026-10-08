import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    add(nums=[0] * 100000, k=100000)
    add(nums=[-100000, 100000] * 50000, k=-100000)
    while len(calls) < 600:
        n = rng.randint(2, 45)
        nums = [rng.randint(-10, 10) for _ in range(n)]
        if len(calls) % 3 == 0:
            nums = [0] * n
            nums[rng.randrange(n)] = rng.randint(-100000, 100000)
            k = 0
        else:
            k = (
                rng.randint(-100000, 100000)
                if len(calls) % 5 == 0
                else rng.randint(-15, 15)
            )
        assert 2 <= n <= 100000 and all(-100000 <= x <= 100000 for x in nums + [k])
        add(nums=nums, k=k)
    assert len(calls) == 600
    return list(calls)
