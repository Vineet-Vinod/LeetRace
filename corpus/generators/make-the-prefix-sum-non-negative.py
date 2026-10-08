def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            "candidate(nums=[2, 3, -5, 4])",
            "candidate(nums=[3, -5, -2, 6])",
            f"candidate(nums={[-1] * 50000 + [1] * 50000!r})",
            "candidate(nums=[-1000000000, 1000000000])",
        ]
    )
    for index in range(600):
        size = 1 + index % 1000
        nums = [rng.randint(-1000, 1000) for _ in range(size)]
        if sum(nums) < 0:
            nums[-1] += -sum(nums)
        cases.add(f"candidate(nums={nums!r})")
    while len(cases) < 600:
        nums = [rng.randint(-1000, 1000) for _ in range(rng.randint(1, 100))]
        if sum(nums) < 0:
            nums[-1] -= sum(nums)
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
