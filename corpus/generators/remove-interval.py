def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {"candidate(intervals=[[0,2],[3,4],[5,7]],toBeRemoved=[1,6])"}
    while len(cases) < 600:
        n = rng.randint(1, 20)
        intervals = []
        start = rng.randint(-100, 0)
        for _ in range(n):
            end = start + rng.randint(1, 10)
            intervals.append([start, end])
            start = end + rng.randint(1, 5)
        left = rng.randint(-110, 150)
        right = left + rng.randint(1, 20)
        cases.add(f"candidate(intervals={intervals!r},toBeRemoved={[left, right]!r})")
    return sorted(cases)
