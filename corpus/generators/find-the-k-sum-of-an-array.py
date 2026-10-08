import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def valid(nums, k):
        return (
            1 <= len(nums) <= 100000
            and 1 <= k <= min(2000, 2 ** len(nums))
            and all(-(10**9) <= x <= 10**9 for x in nums)
        )

    def emit(**args):
        assert valid(**args), args
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in args.items()) + ")"
        calls[call] = None

    emit(nums=[2, 4, -2], k=5)
    emit(nums=[1, -2, 3, 4, -10, 12], k=16)
    emit(nums=[10**9, -(10**9)] * 50000, k=2000)
    emit(nums=[0] * 100000, k=2000)
    while len(calls) < 600:
        n = rng.randint(1, 18)
        nums = [rng.randint(-30, 30) for _ in range(n)]
        k = rng.randint(1, min(2000, 2**n))
        emit(nums=nums, k=k)
    assert len(calls) == 600
    return list(calls)
