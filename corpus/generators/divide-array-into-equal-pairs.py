import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        pair_count = rng.randint(1, 500)
        nums = [rng.randint(1, 500) for _ in range(pair_count)]
        nums = [value for value in nums for _ in range(2)]
        if rng.randrange(2):
            nums[0] = rng.randint(1, 500)
            if nums.count(nums[0]) % 2 == 0:
                nums[-1] = (nums[-1] % 500) + 1
        rng.shuffle(nums)
        calls.add(f"candidate(nums={nums!r})")
    return sorted(calls)
