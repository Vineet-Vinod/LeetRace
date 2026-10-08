def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            "candidate(height=[1, 8, 6, 2, 5, 4, 8, 3, 7])",
            "candidate(height=[1, 1])",
            "candidate(height=[10000 if i % 2 else 0 for i in range(100000)])",
        ]
    )
    for index in range(600):
        size = 2 + index % 200
        height = [rng.randint(0, 10000) for _ in range(size)]
        if index % 4 == 0:
            height = sorted(height)
        elif index % 4 == 1:
            height.sort(reverse=True)
        cases.add(f"candidate(height={height!r})")
    while len(cases) < 600:
        height = [rng.randint(0, 10000) for _ in range(rng.randint(2, 50))]
        cases.add(f"candidate(height={height!r})")
    return sorted(cases)
