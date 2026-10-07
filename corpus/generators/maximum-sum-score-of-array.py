def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(nums=[4, 3, -2, 5])", "candidate(nums=[-3, -5])"])
    for index in range(600):
        size = 100000 if index == 0 else 1 + index % 500
        nums = [rng.randint(-100000, 100000) for _ in range(size)]
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
