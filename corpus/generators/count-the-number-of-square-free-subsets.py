def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            "candidate(nums=[3, 4, 4, 5])",
            "candidate(nums=[1])",
            f"candidate(nums={[1] * 1000!r})",
            f"candidate(nums={[30] * 1000!r})",
        ]
    )
    for index in range(600):
        size = 1 + index % 100
        nums = [rng.randint(1, 30) for _ in range(size)]
        if index % 50 == 0:
            nums = [1] * min(1000, size * 10) + nums
        cases.add(f"candidate(nums={nums!r})")
    while len(cases) < 600:
        nums = [rng.randint(1, 30) for _ in range(rng.randint(1, 100))]
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
