import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        n = rng.randint(1, 60)
        queue = [[rng.randint(0, 30), 0] for _ in range(n)]
        for i, (height, _) in enumerate(queue):
            queue[i][1] = sum(1 for prior, _ in queue[:i] if prior >= height)
        people = [row[:] for row in queue]
        rng.shuffle(people)
        key = tuple(map(tuple, people))
        if key not in seen:
            seen.add(key)
            assert all(0 <= h <= 10**6 and 0 <= k < n for h, k in people)
            cases.append(f"candidate(people={people!r})")
    return cases
