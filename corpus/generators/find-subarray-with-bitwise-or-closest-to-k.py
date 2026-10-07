import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(nums, k):
        assert (
            1 <= len(nums) <= 100000
            and all(1 <= v <= 10**9 for v in nums)
            and 1 <= k <= 10**9
        )

    add(nums=[1, 2, 4, 5], k=3)
    while len(calls) < 598:
        nums = [rng.randint(1, 1023) for _ in range(rng.randint(1, 40))]
        k = rng.randint(1, 2047)
        if len(calls) % 3 == 0:
            a = rng.randrange(len(nums))
            b = rng.randrange(a, len(nums))
            k = 0
            for v in nums[a : b + 1]:
                k |= v
        if len(calls) % 3 == 1:
            nums = [1 << rng.randrange(29) for _ in nums]
            k = rng.randint(1, 10**9)
        add(nums=nums, k=k)
    calls["candidate(nums=[1000000000]*100000, k=1)"] = None
    calls["candidate(nums=[1]*100000, k=1000000000)"] = None
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
