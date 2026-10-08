import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {(1, 1), (1, 2, 2), (3, 1, 3, 4, 2), (3, 3, 3, 3, 3)}
    while len(cases) < 600:
        n = rng.randint(1, 100)
        duplicate = rng.randint(1, n)
        nums = list(range(1, n + 1))
        nums.remove(duplicate)
        nums.extend([duplicate] * rng.randint(2, 5))
        rng.shuffle(nums)
        cases.add(tuple(nums))
    assert all(
        len(nums) >= 2
        and (n := len(nums) - 1) <= 100_000
        and all(1 <= value <= n for value in nums)
        and sum(count > 1 for count in __import__("collections").Counter(nums).values())
        == 1
        for nums in cases
    )
    return [f"candidate(nums={list(nums)!r})" for nums in sorted(cases)]
