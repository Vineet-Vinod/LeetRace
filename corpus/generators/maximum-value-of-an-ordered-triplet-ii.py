def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(nums=[12, 6, 1, 2, 7])", "candidate(nums=[1, 2, 3])"])
    for index in range(600):
        size = 100000 if index == 0 else 3 + index % 500
        nums = [rng.randint(1, 1000000) for _ in range(size)]
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
