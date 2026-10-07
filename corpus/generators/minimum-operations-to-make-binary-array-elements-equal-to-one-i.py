def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            "candidate(nums=[0, 1, 1, 1, 0, 0])",
            "candidate(nums=[0] * 100000)",
            "candidate(nums=[1] * 100000)",
        ]
    )
    for index in range(600):
        size = 3 + index % 1000
        nums = [rng.randrange(2) for _ in range(size)]
        if index % 4 == 0:
            nums = [1] * size
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
