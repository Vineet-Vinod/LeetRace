import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(nums, k):
        assert 1 <= len(nums) <= 100000 and all(1 <= x <= 10**9 for x in nums)
        assert 0 <= k <= 10**14

    add(nums=[1, 2, 6, 4], k=3)
    add(nums=[1, 4, 4, 2, 4], k=0)
    while len(calls) < 598:
        n = rng.randint(1, 40)
        mode = len(calls) % 4
        nums = [rng.randint(1, 30 if mode < 3 else 10**9) for _ in range(n)]
        if mode == 0:
            nums = [rng.randint(1, 100)] * n
        add(nums=nums, k=rng.choice([0, 1, rng.randint(1, 500), 10**14]))
    calls["candidate(nums=[1]*100000, k=0)"] = None
    calls["candidate(nums=[1,1000000000]*50000, k=100000000000000)"] = None
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
