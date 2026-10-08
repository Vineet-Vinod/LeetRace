import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(nums, **bounds):
        lower_bound = bounds["l"]
        upper_bound = bounds["r"]
        assert (
            1 <= len(nums) <= 20000
            and all(0 <= v <= 20000 for v in nums)
            and sum(nums) <= 20000
        )
        assert 0 <= lower_bound <= upper_bound <= 20000

    add(nums=[1, 2, 2, 3], l=6, r=6)
    while len(calls) < 597:
        nums = [rng.randint(0, 20) for _ in range(rng.randint(1, 40))]
        lower_bound = rng.randint(0, sum(nums) + 10)
        upper_bound = rng.randint(lower_bound, min(20000, lower_bound + 100))
        if len(calls) % 3 == 0:
            lower_bound = 0
            upper_bound = sum(nums)
        add(nums=nums, l=lower_bound, r=upper_bound)
    calls["candidate(nums=[0]*20000, l=0, r=20000)"] = None
    calls["candidate(nums=[1]*20000, l=0, r=20000)"] = None
    calls["candidate(nums=[20000], l=20000, r=20000)"] = None
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
