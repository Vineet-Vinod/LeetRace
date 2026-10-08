import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    add(nums=[100000] * 100000)
    add(nums=list(range(100000, 0, -1)))
    for nums in ([5, 2, 2], [1], [4, 3, 2, 6], [1, 2, 3, 4]):
        add(nums=nums)
    while len(calls) < 600:
        nums = [
            rng.randint(1, 100000 if len(calls) % 5 == 0 else 30)
            for _ in range(rng.randint(1, 45))
        ]
        if len(calls) % 4 == 0:
            nums.sort()
        if len(calls) % 4 == 1:
            nums.sort(reverse=True)
        assert 1 <= len(nums) <= 100000 and all(1 <= x <= 100000 for x in nums)
        add(nums=nums)
    assert len(calls) == 600
    return list(calls)
