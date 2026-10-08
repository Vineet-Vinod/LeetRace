def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(nums=[2, -1, -4, -3])"])
    for index in range(600):
        size = 100000 if index == 0 else 1 + index % 300
        nums = [rng.randint(-10000, 10000) for _ in range(size)]
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
