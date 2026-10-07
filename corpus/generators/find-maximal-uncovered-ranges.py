def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(
        [
            "candidate(n=10, ranges=[[3, 5], [7, 8]])",
            "candidate(n=3, ranges=[[0, 2]])",
            "candidate(n=7, ranges=[[2, 4], [0, 3]])",
            "candidate(n=1000000000, ranges=[])",
            "candidate(n=1000000000, ranges=[[i, i] for i in range(1000000)])",
        ]
    )
    for index in range(600):
        n = 1 + index % 500
        ranges = []
        for _ in range(rng.randint(0, min(80, n))):
            left = rng.randrange(n)
            right = rng.randrange(left, n)
            ranges.append([left, right])
        cases.add(f"candidate(n={n}, ranges={ranges!r})")
    while len(cases) < 600:
        n = rng.randint(1, 1000)
        ranges = []
        for _ in range(rng.randint(0, 100)):
            left = rng.randrange(n)
            ranges.append([left, rng.randrange(left, n)])
        cases.add(f"candidate(n={n}, ranges={ranges!r})")
    return sorted(cases)
