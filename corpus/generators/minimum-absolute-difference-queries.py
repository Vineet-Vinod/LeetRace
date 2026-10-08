def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            "candidate(nums=[1, 3, 4, 8], queries=[[0, 1], [1, 2], [2, 3]])",
            "candidate(nums=[i % 100 + 1 for i in range(100000)], queries=[[i % 99999, 99999] for i in range(20000)])",
        ]
    )
    for index in range(600):
        size = 2 + index % 200
        nums = [rng.randint(1, 100) for _ in range(size)]
        queries = []
        for _ in range(1 + index % 20):
            left = rng.randrange(size - 1)
            queries.append([left, rng.randrange(left + 1, size)])
        cases.add(f"candidate(nums={nums!r}, queries={queries!r})")
    while len(cases) < 600:
        size = rng.randint(2, 200)
        nums = [rng.randint(1, 100) for _ in range(size)]
        left = rng.randrange(size - 1)
        cases.add(
            f"candidate(nums={nums!r}, queries=[[{left}, {rng.randrange(left + 1, size)}]])"
        )
    return sorted(cases)
