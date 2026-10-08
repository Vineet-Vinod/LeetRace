import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def valid(nums):
        return 1 <= len(nums) <= 100000 and all(1 <= x <= 10**9 for x in nums)

    def emit(**args):
        assert valid(**args), args
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in args.items()) + ")"
        calls[call] = None

    for nums in [
        [12, 5, 7, 23],
        [29, 6, 10],
        [3, 6],
        [1],
        [10**9],
        [10**9] * 100000,
        [1] + [10**9] * 99999,
    ]:
        emit(nums=nums)
    while len(calls) < 600:
        n = rng.randint(1, 40)
        mode = rng.randrange(3)
        if mode == 0:
            factor = rng.randint(2, 1000)
            nums = [factor * rng.randint(1, 10000) for _ in range(n)]
        elif mode == 1:
            nums = [rng.randint(1, 10**9) for _ in range(n)]
            nums[0] = 1
        else:
            nums = [rng.randint(1, 10000) for _ in range(n)]
        emit(nums=nums)
    assert len(calls) == 600
    return list(calls)
