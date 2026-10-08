import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(nums: list[int], k: int) -> None:
        assert (
            1 <= len(nums) <= 20000
            and 1 <= k <= len(nums)
            and all(1 <= x <= len(nums) for x in nums)
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in [("nums", nums), ("k", k)])
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(nums=[1, 2, 1, 2, 3], k=2)
    add(nums=[1] * 20000, k=1)
    add(nums=list(range(1, 20001)), k=20000)
    add(nums=[20000] * 20000, k=20000)
    add(nums=[1, 2, 1, 2, 3], k=2)
    add(nums=[1, 2, 1, 3, 4], k=3)
    while len(calls) < 600:
        n = rng.randint(1, 60)
        cap = rng.randint(1, n)
        nums = [rng.randint(1, cap) for _ in range(n)]
        add(nums=nums, k=rng.choice([1, n, rng.randint(1, cap)]))
    return calls
