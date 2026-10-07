import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        nums, t = kwargs["nums"], kwargs["threshold"]
        assert (
            1 <= len(nums) <= 100000
            and all(1 <= v <= 10**9 for v in nums)
            and 1 <= t <= 10**9
        )
        call = "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(nums=[1] * 100000, threshold=99999)
    add(nums=[1] * 100000, threshold=100000)
    add(nums=[10**9] * 100000, threshold=10**9)
    add(nums=[1, 3, 4, 3, 1], threshold=6)
    add(nums=[1, 3, 4, 3, 1], threshold=6)
    add(nums=[6, 5, 6, 5, 8], threshold=7)
    while len(calls) < 600:
        n = rng.randint(1, 60)
        mode = rng.randrange(3)
        nums = [rng.randint(1, 1000) for _ in range(n)]
        if mode == 0:
            a = rng.randrange(n)
            b = rng.randint(a, n - 1)
            threshold = max(1, min(nums[a : b + 1]) * (b - a + 1) - 1)
        elif mode == 1:
            threshold = max(nums) * n
        else:
            threshold = rng.randint(1, 10000)
        add(nums=nums, threshold=threshold)
    return calls
