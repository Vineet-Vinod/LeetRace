def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            "candidate(candies=[1, 2, 2, 3, 4, 3], k=3)",
            "candidate(candies=[2, 4, 5], k=0)",
            "candidate(candies=[i % 10000 + 1 for i in range(100000)], k=50000)",
            "candidate(candies=[100000 if i == 0 else 1 for i in range(100000)], k=100000)",
        ]
    )
    for index in range(600):
        size = index % 1000
        candies = [rng.randint(1, max(1, size // 2 + 1)) for _ in range(size)]
        k = rng.randint(0, size)
        cases.add(f"candidate(candies={candies!r}, k={k})")
    return sorted(cases)
