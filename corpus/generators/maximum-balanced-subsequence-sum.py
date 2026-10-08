import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def valid(nums):
        return 1 <= len(nums) <= 100000 and all(-(10**9) <= x <= 10**9 for x in nums)

    def emit(**args):
        assert valid(**args), args
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in args.items()) + ")"
        calls[call] = None

    for nums in [
        [3, 3, 5, 6],
        [5, -1, -3, 8],
        [-2, -1],
        [10**9] * 100000,
        list(range(100000)),
        [-(10**9)] * 100000,
    ]:
        emit(nums=nums)
    while len(calls) < 600:
        n = rng.randint(1, 60)
        mode = rng.randrange(4)
        nums = [rng.randint(-100, 100) for _ in range(n)]
        if mode == 0:
            nums = [-rng.randint(1, 1000) for _ in range(n)]
        elif mode == 1:
            start = rng.randint(-100, 100)
            nums = [start + i for i in range(n)]
        elif mode == 2:
            nums = sorted(nums, reverse=True)
        emit(nums=nums)
    assert len(calls) == 600
    return list(calls)
