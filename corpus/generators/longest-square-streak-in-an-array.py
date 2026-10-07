def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            "candidate(nums=[4, 3, 6, 16, 8, 2])",
            f"candidate(nums={[2 + (i % 99999) for i in range(100000)]!r})",
        ]
    )
    for index in range(600):
        size = 2 + index % 100
        nums = [rng.randint(2, 100000) for _ in range(size)]
        if index % 4 == 0:
            start = rng.randint(2, 10)
            nums[: min(4, size)] = [start, start * start, start**4, start**8][
                : min(4, size)
            ]
            nums = [min(value, 100000) for value in nums]
        cases.add(f"candidate(nums={nums!r})")
    while len(cases) < 600:
        nums = [rng.randint(2, 100000) for _ in range(rng.randint(2, 100))]
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
