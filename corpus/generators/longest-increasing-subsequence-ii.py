import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(nums: list[int], k: int) -> None:
        assert (
            1 <= len(nums) <= 100000
            and 1 <= k <= 100000
            and all(1 <= x <= 100000 for x in nums)
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in [("nums", nums), ("k", k)])
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(nums=[4, 2, 1, 4, 3, 4, 5, 8, 15], k=3)
    add(nums=list(range(1, 100001)), k=1)
    add(nums=[100000] * 100000, k=100000)
    add(nums=list(range(100000, 0, -1)), k=100000)
    add(nums=[4, 2, 1, 4, 3, 4, 5, 8, 15], k=3)
    add(nums=[7, 4, 5, 1, 8, 12, 4, 7], k=5)
    add(nums=[1, 5], k=1)
    while len(calls) < 600:
        n = rng.randint(1, 45)
        nums = [rng.randint(1, 100) for _ in range(n)]
        if len(calls) % 4 == 0:
            nums.sort()
        add(nums=nums, k=rng.choice([1, 100000, rng.randint(1, 100)]))
    return calls
