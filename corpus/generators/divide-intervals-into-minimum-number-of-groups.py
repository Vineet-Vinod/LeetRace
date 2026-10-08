def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set(["candidate(intervals=[[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]])"])
    for index in range(600):
        size = 100000 if index % 250 == 0 else 1 + index % 100
        intervals = []
        for _ in range(size):
            left = rng.randint(1, 999999)
            right = rng.randint(left, 1000000)
            intervals.append([left, right])
        cases.add(f"candidate(intervals={intervals!r})")
    while len(cases) < 600:
        intervals = []
        for _ in range(rng.randint(1, 100)):
            left = rng.randint(1, 999999)
            intervals.append([left, rng.randint(left, 1000000)])
        cases.add(f"candidate(intervals={intervals!r})")
    return sorted(cases)
