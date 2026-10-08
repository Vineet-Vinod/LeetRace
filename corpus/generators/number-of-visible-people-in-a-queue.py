import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(heights):
        assert (
            1 <= len(heights) <= 100000
            and len(set(heights)) == len(heights)
            and all(1 <= v <= 100000 for v in heights)
        )

    add(heights=[10, 6, 8, 5, 11, 9])
    add(heights=[5, 1, 2, 3, 10])
    while len(calls) < 597:
        nums = rng.sample(range(1, 100001), rng.randint(1, 50))
        mode = len(calls) % 3
        if mode == 0:
            nums.sort()
        if mode == 1:
            nums.sort(reverse=True)
        add(heights=nums)
    calls["candidate(heights=list(range(1,100001)))"] = None
    calls["candidate(heights=list(range(100000,0,-1)))"] = None
    calls["candidate(heights=[100000]+list(range(1,100000)))"] = None
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
