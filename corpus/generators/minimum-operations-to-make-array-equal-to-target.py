import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(nums, target):
        assert 1 <= len(nums) == len(target) <= 100000 and all(
            1 <= v <= 100000000 for v in nums + target
        )

    add(nums=[3, 5, 1, 2], target=[4, 6, 2, 4])
    add(nums=[1, 3, 2], target=[2, 1, 4])
    while len(calls) < 598:
        n = rng.randint(1, 50)
        nums = [rng.randint(1, 100) for _ in range(n)]
        target = [rng.randint(1, 100) for _ in nums]
        if len(calls) % 4 == 0:
            target = nums[:]
        if len(calls) % 4 == 1:
            target = [v + rng.randint(1, 1000000) for v in nums]
        add(nums=nums, target=target)
    calls["candidate(nums=[1]*100000, target=[100000000]*100000)"] = None
    calls["candidate(nums=[1,100000000]*50000, target=[100000000,1]*50000)"] = None
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
