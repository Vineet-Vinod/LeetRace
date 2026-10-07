import random


def generate(seed: int = 0) -> list[str]:
    """Generate seeded calls satisfying: n1..10^5; rides1..3*10^4 with 1<=start<end<=n and positive tips."""
    rng = random.Random(seed)
    calls = {"candidate(n=5, rides=[[2, 5, 4], [1, 5, 1]])"}
    while len(calls) < 600:
        n = rng.randint(2, 100)
        rides = []
        for _ in range(rng.randint(1, 80)):
            start = rng.randint(1, n - 1)
            end = rng.randint(start + 1, n)
            rides.append([start, end, rng.randint(1, 1000)])
        calls.add(f"candidate(n={n}, rides={rides!r})")
    return sorted(calls)
