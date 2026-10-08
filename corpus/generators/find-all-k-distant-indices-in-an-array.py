import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int, int]] = {
        ((1,), 1, 1),
        ((3, 4, 9, 1, 3, 9, 5), 9, 1),
    }
    cases.add(((1000,) * 1000, 1000, 1000))
    while len(cases) < 600:
        size = rng.randint(1, 1000)
        nums = [rng.randint(1, 1000) for _ in range(size)]
        key = nums[rng.randrange(size)]
        cases.add((tuple(nums), key, rng.randint(1, size)))
    calls = [
        f"candidate(nums={list(nums)!r}, key={key}, k={k})" for nums, key, k in cases
    ]
    calls.extend(["candidate(nums=[2, 2, 2, 2, 2], key=2, k=2)"])
    return list(dict.fromkeys(calls))
