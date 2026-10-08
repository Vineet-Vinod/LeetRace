import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], tuple[int, ...]]] = {
        ((0, 1, 2, 3, 4), (0, 1, 2, 2, 1)),
        ((1,), (0,)),
    }
    cases.add((tuple(range(99)) + (100,), tuple(range(99)) + (99,)))
    while len(cases) < 600:
        size = rng.randint(1, 100)
        nums = tuple(rng.randint(0, 100) for _ in range(size))
        positions = tuple(rng.randint(0, i) for i in range(size))
        cases.add((nums, positions))
    calls = [
        f"candidate(nums={list(nums)!r}, index={list(index)!r})"
        for nums, index in cases
    ]
    calls.extend(["candidate(nums=[1, 2, 3, 4, 0], index=[0, 1, 2, 3, 0])"])
    return list(dict.fromkeys(calls))
