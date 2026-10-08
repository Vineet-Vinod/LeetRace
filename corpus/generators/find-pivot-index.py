import random


def _pivot(nums: list[int]) -> int:
    for index in range(len(nums)):
        if sum(nums[:index]) == sum(nums[index + 1 :]):
            return index
    return -1


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    with_pivot: set[str] = {
        "candidate(nums=[1, 7, 3, 6, 5, 6])",
        "candidate(nums=[2, 1, -1])",
        "candidate(nums=[0])",
    }
    without_pivot: set[str] = {
        "candidate(nums=[1, 2, 3])",
        "candidate(nums=[1, 2])",
        "candidate(nums=[1, 1, 2])",
    }
    while len(with_pivot) < 300:
        left = [rng.randint(-20, 20) for _ in range(rng.randint(0, 20))]
        right = [rng.randint(-20, 20) for _ in range(rng.randint(0, 19))]
        right.append(sum(left) - sum(right))
        nums = left + [rng.randint(-1000, 1000)] + right
        if -1000 <= right[-1] <= 1000 and _pivot(nums) >= 0:
            with_pivot.add(f"candidate(nums={nums!r})")
    while len(without_pivot) < 300:
        nums = [rng.randint(-20, 20) for _ in range(rng.randint(2, 50))]
        if _pivot(nums) == -1:
            without_pivot.add(f"candidate(nums={nums!r})")
    return sorted(with_pivot | without_pivot)
