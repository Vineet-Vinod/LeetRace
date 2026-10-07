def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        ["candidate(nums=[5, 0, 3, 8, 6])", "candidate(nums=[1, 1, 1, 0, 6, 12])"]
    )
    for index in range(600):
        size = 100000 if index == 0 else 2 + index % 500
        split = rng.randint(1, size - 1)
        left = [rng.randint(0, 1000000) for _ in range(split)]
        right = [rng.randint(max(left), 1000000) for _ in range(size - split)]
        nums = left + right
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
