def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(nums=[2, 1, 3, 4, 5, 2])"])
    for index in range(600):
        size = 100000 if index == 0 else 1 + index % 1000
        nums = [rng.randint(1, 1000000) for _ in range(size)]
        if index % 4 == 0:
            nums = [1] * size
        cases.add(f"candidate(nums={nums!r})")
    while len(cases) < 600:
        nums = [rng.randint(1, 1000000) for _ in range(rng.randint(1, 100))]
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
