import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def valid(nums, indexDiff, valueDiff):
        return (
            2 <= len(nums) <= 100000
            and 1 <= indexDiff <= len(nums)
            and 0 <= valueDiff <= 10**9
            and all(-(10**9) <= x <= 10**9 for x in nums)
        )

    def emit(**args):
        assert valid(**args), args
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in args.items()) + ")"
        calls[call] = None

    emit(nums=[1, 2, 3, 1], indexDiff=3, valueDiff=0)
    emit(nums=[1, 5, 9, 1, 5, 9], indexDiff=2, valueDiff=3)
    emit(nums=list(range(100000)), indexDiff=100000, valueDiff=0)
    emit(nums=[-(10**9), 10**9], indexDiff=2, valueDiff=10**9)
    while len(calls) < 600:
        n = rng.randint(2, 40)
        indexDiff = rng.randint(1, n)
        valueDiff = rng.choice([0, 1, 5, 100, rng.randint(0, 10**9)])
        if rng.randrange(2):
            nums = [rng.randint(-(10**9), 10**9) for _ in range(n)]
            nums[1] = nums[0]
        else:
            step = valueDiff + 1
            if (n - 1) * step > 2 * 10**9:
                valueDiff = 1
                step = 2
            nums = [-(10**9) + i * step for i in range(n)]
        emit(nums=nums, indexDiff=indexDiff, valueDiff=valueDiff)
    assert len(calls) == 600
    return list(calls)
