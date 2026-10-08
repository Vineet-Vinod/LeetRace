import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(nums):
        assert 1 <= len(nums) <= 50000 and all(
            -2147483648 <= v <= 2147483647 for v in nums
        )
        call = (
            "candidate("
            + ", ".join(f"{name}={value!r}" for name, value in (("nums", nums),))
            + ")"
        )
        calls[call] = None

    add(nums=[1, 3, 2, 3, 1])
    add(nums=[2, 4, 3, 5, 1])
    add(nums=[-2147483648] * 50000)
    add(nums=list(range(50000)))
    add(nums=[2147483647, -2147483648] * 25000)
    while len(calls) < 600:
        n = rng.randint(1, 75)
        mode = rng.randrange(5)
        nums = [rng.randint(-1000, 1000) for _ in range(n)]
        if mode == 0:
            nums = [rng.randint(-2147483648, 2147483647) for _ in range(n)]
        elif mode == 1:
            nums.sort()
        elif mode == 2:
            nums = [rng.randint(-100, 100)] * n
        elif mode == 3:
            nums = [rng.choice((-2147483648, 2147483647, 0, -1, 1)) for _ in range(n)]
        add(nums=nums)
    return list(calls)
