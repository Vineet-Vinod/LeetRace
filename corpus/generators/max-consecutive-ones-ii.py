def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            "candidate(nums=[1, 0, 1, 1, 0])",
            "candidate(nums=[1, 0, 1, 1, 0, 1])",
            f"candidate(nums={[1] * 100000!r})",
            f"candidate(nums={[0] * 100000!r})",
        ]
    )
    for index in range(600):
        size = 1 + index % 1000
        nums = [rng.randrange(2) for _ in range(size)]
        if index % 3 == 0:
            nums = [1] * size
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
