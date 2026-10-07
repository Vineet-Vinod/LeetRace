import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(nums):
        assert 1 <= len(nums) <= 100000 and all(1 <= v <= 1000000000 for v in nums)

    add(nums=[2, 1, 4])
    add(nums=[1, 1, 1])
    while len(calls) < 598:
        n = rng.randint(1, 40)
        nums = [rng.randint(1, 20 if len(calls) % 2 else 10**9) for _ in range(n)]
        if len(calls) % 3 == 0:
            nums = [rng.randint(1, 10**9)] * n
        add(nums=nums)
    calls["candidate(nums=[1]*100000)"] = None
    calls["candidate(nums=[1000000000]*100000)"] = None
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
