import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(nums, cost):
        assert 1 <= len(nums) == len(cost) <= 100000 and all(
            1 <= v <= 1000000 for v in nums + cost
        )
        # Any fixed endpoint is an upper bound on the optimum, enforce promised result <= 2^53-1.
        assert (
            min(
                sum(abs(v - t) * c for v, c in zip(nums, cost))
                for t in [min(nums), max(nums)]
            )
            <= 2**53 - 1
        )

    add(nums=[1, 3, 5, 2], cost=[2, 3, 1, 14])
    add(nums=[2] * 5, cost=[4, 2, 8, 1, 3])
    while len(calls) < 598:
        n = rng.randint(1, 40)
        nums = [rng.randint(1, 1000000) for _ in range(n)]
        cost = [rng.randint(1, 1000000) for _ in nums]
        if len(calls) % 3 == 0:
            nums = [rng.randint(1, 1000000)] * n
        add(nums=nums, cost=cost)
    calls["candidate(nums=[1]*100000, cost=[1000000]*100000)"] = None
    calls["candidate(nums=[1,1000000]*50000, cost=[1]*100000)"] = None
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
