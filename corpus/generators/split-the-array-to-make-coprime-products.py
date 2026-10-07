import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(nums):
        assert 1 <= len(nums) <= 10000 and all(1 <= v <= 1000000 for v in nums)

    add(nums=[4, 7, 8, 15, 3, 5])
    add(nums=[4, 7, 15, 8, 3, 5])
    add(nums=[1])
    while len(calls) < 597:
        nums = [
            rng.randint(1, 1000000 if len(calls) % 3 == 0 else 100)
            for _ in range(rng.randint(1, 40))
        ]
        if len(calls) % 3 == 1:
            nums = [2 * rng.randint(1, 50) for _ in nums]
        if len(calls) % 3 == 2:
            nums = [2 ** rng.randint(0, 19)] + [
                3 ** rng.randint(0, 12) for _ in nums[1:]
            ]
        add(nums=nums)
    calls["candidate(nums=[1000000]*10000)"] = None
    calls["candidate(nums=[1]*10000)"] = None
    calls["candidate(nums=[999983]+[2]*9999)"] = None
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
