def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(nums=[1, 1, 1, 1, 1], target=2)"])
    for index in range(600):
        size = 100000 if index == 0 else 1 + index % 500
        nums = [rng.randint(-10000, 10000) for _ in range(size)]
        target = rng.randint(0, 1000000)
        if index % 4 == 0:
            nums = [1] * size
            target = rng.randint(0, size)
        cases.add(f"candidate(nums={nums!r}, target={target})")
    return sorted(cases)
