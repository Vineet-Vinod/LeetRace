def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(nums=[3, 2, 4, 4, 1], costs=[3, 7, 6, 4, 2])"])
    for index in range(600):
        size = 100000 if index == 0 else 1 + index % 200
        nums = [rng.randint(0, 100000) for _ in range(size)]
        costs = [rng.randint(0, 100000) for _ in range(size)]
        cases.add(f"candidate(nums={nums!r}, costs={costs!r})")
    return sorted(cases)
