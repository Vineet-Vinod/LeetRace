def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(nums=[7, 6, 5, 4, 3, 2, 1, 6, 10, 11])"])
    for index in range(600):
        size = 100000 if index == 0 else 1 + index % 1000
        nums = [rng.randint(-(10**9), 10**9) for _ in range(size)]
        if index % 3 == 0:
            nums.sort()
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
