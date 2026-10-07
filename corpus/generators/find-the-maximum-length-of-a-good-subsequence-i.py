def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            "candidate(nums=[1, 2, 1, 1, 3], k=2)",
            "candidate(nums=[1, 2, 3, 4, 5, 1], k=0)",
            f"candidate(nums={[i % 1000000000 + 1 for i in range(500)]!r}, k=25)",
            "candidate(nums=[1, 1000000000] * 250, k=25)",
        ]
    )
    for index in range(600):
        size = 1 + index % 100
        nums = [rng.randint(1, 10**9) for _ in range(size)]
        if index % 4 == 0:
            nums = [rng.randint(1, 5) for _ in range(size)]
        k = rng.randint(0, min(size, 25))
        cases.add(f"candidate(nums={nums!r}, k={k})")
    while len(cases) < 600:
        nums = [rng.randint(1, 10**9) for _ in range(rng.randint(1, 100))]
        cases.add(f"candidate(nums={nums!r}, k={rng.randint(0, min(len(nums), 25))})")
    return sorted(cases)
