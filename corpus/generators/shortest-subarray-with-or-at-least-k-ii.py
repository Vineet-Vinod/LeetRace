import random


def generate(seed: int = 0) -> list[str]:
    r = random.Random(seed)
    cases = []
    seen = set()

    def add(nums, k):
        key = (tuple(nums), k)
        if key not in seen:
            assert (
                1 <= len(nums) <= 200_000
                and all(0 <= x <= 10**9 for x in nums)
                and 0 <= k <= 10**9
            )
            seen.add(key)
            cases.append(f"candidate(nums={nums!r}, k={k})")

    add([0], 0)
    add([0], 1)
    add([1] * 200_000, 1)
    add([1] * 200_000, 2)
    for width in range(1, 30):
        nums = [1 << i for i in range(width)]
        add(nums, (1 << width) - 1)
        add(nums, 1 << width)
    for _ in range(300):
        n = r.randint(1, 100)
        nums = [r.randint(0, 1000) for _ in range(n)]
        whole = 0
        for x in nums:
            whole |= x
        k = r.randint(0, whole)
        add(nums, k)
    for _ in range(300):
        n = r.randint(1, 100)
        nums = [r.randint(0, 2**20 - 1) for _ in range(n)]
        add(nums, 1 << 21)
    return cases
