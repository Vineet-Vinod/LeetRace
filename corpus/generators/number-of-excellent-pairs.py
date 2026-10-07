import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def valid(nums, k):
        return (
            1 <= len(nums) <= 100000
            and all(1 <= x <= 10**9 for x in nums)
            and 1 <= k <= 60
        )

    def emit(**args):
        assert valid(**args), args
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in args.items()) + ")"
        calls[call] = None

    emit(nums=[1, 2, 3, 1], k=3)
    emit(nums=[5, 1, 1], k=10)
    emit(nums=list(range(1, 100001)), k=20)
    emit(nums=[10**9] * 100000, k=60)
    while len(calls) < 600:
        nums = [
            rng.randint(1, rng.choice([50, 10**9])) for _ in range(rng.randint(1, 40))
        ]
        k = rng.choice([1, 2, 60, rng.randint(1, 40)])
        emit(nums=nums, k=k)
    assert len(calls) == 600
    return list(calls)
