import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def valid(nums):
        return 1 <= len(nums) <= 100000 and all(1 <= x <= 100000 for x in nums)

    def emit(**args):
        assert valid(**args), args
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in args.items()) + ")"
        calls[call] = None

    for nums in [
        [2, 3, 6],
        [3, 9, 5],
        [4, 3, 12, 8],
        [1],
        [1, 1],
        [100000] * 100000,
        [1] + [100000] * 99999,
    ]:
        emit(nums=nums)
    while len(calls) < 600:
        n = rng.randint(1, 40)
        if rng.randrange(2):
            nums = [2 * rng.randint(1, 50000) for _ in range(n)]
        else:
            nums = [
                rng.choice([1, 3, 5, 7, 11, 13, 17, 19]) * rng.choice([1, 3, 5, 7])
                for _ in range(n)
            ]
        emit(nums=nums)
    assert len(calls) == 600
    return list(calls)
