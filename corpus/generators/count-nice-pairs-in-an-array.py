def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            "candidate(nums=[42, 11, 1, 97])",
            "candidate(nums=[1000000000, 0, 1000000000])",
            f"candidate(nums={[0] * 100000!r})",
        ]
    )
    for index in range(600):
        size = 1 + index % 100
        nums = [rng.randint(0, 10**9) for _ in range(size)]
        if index % 3 == 0:
            nums = [rng.randint(0, 999) for _ in range(size)]
        cases.add(f"candidate(nums={nums!r})")
    while len(cases) < 600:
        nums = [rng.randint(0, 10**9) for _ in range(rng.randint(1, 50))]
        cases.add(f"candidate(nums={nums!r})")
    return sorted(cases)
