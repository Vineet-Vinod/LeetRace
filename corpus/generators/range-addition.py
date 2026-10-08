def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(length=5, updates=[[1, 3, 2], [2, 4, 3], [0, 2, -2]])",
        "candidate(length=1, updates=[])",
        "candidate(length=100000, updates=[[0, 99999, 1000], [50000, 99999, -1000]])",
    }
    while len(cases) < 600:
        length = rng.randint(1, 1000)
        updates = []
        for _ in range(rng.randint(0, 50)):
            start = rng.randrange(length)
            end = rng.randint(start, length - 1)
            updates.append([start, end, rng.randint(-1000, 1000)])
        assert 1 <= length <= 100_000 and len(updates) <= 10_000
        assert all(0 <= a <= b < length and -1000 <= x <= 1000 for a, b, x in updates)
        cases.add(f"candidate(length={length}, updates={updates!r})")
    return sorted(cases)
