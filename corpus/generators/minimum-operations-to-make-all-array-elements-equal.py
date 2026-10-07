import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], tuple[int, ...]]] = {
        ((3, 1, 6, 8), (1, 5)),
        ((2, 9, 6, 3), (10,)),
        ((1,), (1, 10**9)),
        ((1, 10**9), (1, 10**9)),
    }
    cases.add((tuple([10**9] * 100_000), tuple([10**9] * 100_000)))
    while len(cases) < 600:
        nums = tuple(rng.randint(1, 10**9) for _ in range(rng.randint(1, 60)))
        queries = tuple(rng.randint(1, 10**9) for _ in range(rng.randint(1, 60)))
        cases.add((nums, queries))
    assert all(
        1 <= len(nums) <= 100_000
        and 1 <= len(queries) <= 100_000
        and all(1 <= value <= 10**9 for value in nums + queries)
        for nums, queries in cases
    )
    return [
        f"candidate(nums={list(nums)!r}, queries={list(queries)!r})"
        for nums, queries in sorted(cases)
    ]
