def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(nums=[9, 6, 7, 13])", "candidate(nums=[7, 3, 5])"])
    for index in range(600):
        size = 100000 if index == 0 else 1 + index % 1000
        nums = [rng.randint(1, 100000) for _ in range(size)]
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
