import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        validate(**kwargs)
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        calls[call] = None

    def validate(nums, k, maxChanges):
        assert (
            2 <= len(nums) <= 100000
            and set(nums) <= {0, 1}
            and 1 <= k <= 100000
            and 0 <= maxChanges <= 100000
        )
        assert sum(nums) + maxChanges >= k

    add(nums=[1, 1, 0, 0, 0, 1, 1, 0, 0, 1], k=3, maxChanges=1)
    add(nums=[0, 0, 0, 0], k=2, maxChanges=3)
    while len(calls) < 597:
        nums = [rng.randrange(2) for _ in range(rng.randint(2, 45))]
        changes = rng.randint(0, 50)
        if sum(nums) + changes == 0:
            changes = 1
        k = rng.randint(1, sum(nums) + changes)
        add(nums=nums, k=k, maxChanges=changes)
    calls["candidate(nums=[0]*100000, k=100000, maxChanges=100000)"] = None
    calls["candidate(nums=[1]*100000, k=100000, maxChanges=0)"] = None
    calls["candidate(nums=[1]+[0]*99998+[1], k=2, maxChanges=0)"] = None
    # Also validate the evaluated compact expressions used for maximum boundaries.
    for call in calls:
        eval(call, {"candidate": validate})
    return list(calls)
