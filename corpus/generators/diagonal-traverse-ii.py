import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], ...]] = {
        ((1, 2, 3), (4, 5, 6), (7, 8, 9)),
        ((1, 2, 3, 4, 5), (6, 7), (8,), (9, 10, 11), (12, 13, 14, 15, 16)),
        ((1,),),
        ((1, 2, 3),),
        (tuple(range(1, 100_001)),),
    }
    while len(cases) < 600:
        rows = rng.randint(1, 30)
        nums = tuple(
            tuple(rng.randint(1, 100_000) for _ in range(rng.randint(1, 20)))
            for _ in range(rows)
        )
        cases.add(nums)
    assert all(
        1 <= len(nums) <= 100_000
        and 1 <= sum(map(len, nums)) <= 100_000
        and all(
            1 <= len(row) <= 100_000 and all(1 <= value <= 100_000 for value in row)
            for row in nums
        )
        for nums in cases
    )
    return [
        f"candidate(nums={[list(row) for row in nums]!r})" for nums in sorted(cases)
    ]
