import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(nums):
        assert 1 <= len(nums) <= 30000 and all(2 <= v <= 100000 for v in nums)

    add(nums=[7, 21, 3])
    add(nums=[5, 2, 6, 2])
    while len(calls) < 598:
        nums = [rng.randint(2, 100) for _ in range(rng.randint(1, 35))]
        mode = len(calls) % 4
        if mode == 0:
            nums = [2 * rng.randint(1, 50000) for _ in nums]
        if mode == 1:
            nums = sorted(nums)
        if mode == 2:
            nums = rng.sample([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], rng.randint(2, 10))
            nums.sort(reverse=True)
        add(nums=nums)
    calls["candidate(nums=[100000,2]*15000)"] = None
    calls["candidate(nums=[99991]*30000)"] = None
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
