def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        ["candidate(nums=[4, 6, 1, 2], k=2)", "candidate(nums=[1, 1, 1, 1], k=10)"]
    )
    for index in range(600):
        size = 100000 if index == 0 else 1 + index % 500
        nums = [rng.randint(0, 100000) for _ in range(size)]
        k = rng.randint(0, 100000)
        cases.add(f"candidate(nums={nums!r}, k={k})")
    return sorted(cases)
