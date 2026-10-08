def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(nums=[3, 5, 2, 3])"])
    for index in range(600):
        size = 2 * (1 + index % 500)
        if index == 0:
            size = 100000
        nums = [rng.randint(1, 100000) for _ in range(size)]
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
