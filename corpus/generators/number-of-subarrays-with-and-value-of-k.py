import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        nums, k = kwargs["nums"], kwargs["k"]
        assert (
            1 <= len(nums) <= 100000
            and all(0 <= v <= 10**9 for v in nums)
            and 0 <= k <= 10**9
        )
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(nums=[10**9] * 100000, k=10**9)
    add(nums=[0] * 100000, k=0)
    add(nums=[1 << i for i in range(30)] * 3333 + [1] * 10, k=0)
    add(nums=[1, 1, 1], k=1)
    add(nums=[1, 1, 2], k=1)
    add(nums=[1, 2, 3], k=2)
    while len(calls) < 600:
        n = rng.randint(1, 60)
        mode = rng.randrange(4)
        k = rng.randint(0, 255)
        if mode == 0:
            nums = [k] * n
        elif mode == 1:
            nums = [k | rng.randint(0, 255) for _ in range(n)]
            nums[rng.randrange(n)] = k
        elif mode == 2:
            nums = [rng.randint(0, 255) for _ in range(n)]
        else:
            nums = [rng.randint(0, 10**9) for _ in range(n)]
            k = nums[rng.randrange(n)]
        add(nums=nums, k=k)
    return calls
