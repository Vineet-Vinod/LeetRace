import random


def generate(seed: int = 0) -> list[str]:
    """Valid trip counts and strictly increasing pickup/dropoff locations; unique calls."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 1 + i % 18
        trips = []
        for _ in range(n):
            start = rng.randrange(0, 50)
            end = rng.randrange(start + 1, 60)
            trips.append([rng.randrange(1, 9), start, end])
        cap = 1 + (i * 13) % 30
        assert all(1 <= p <= 100 and 0 <= a < b <= 1000 for p, a, b in trips)
        call = f"candidate(trips={trips!r}, capacity={cap})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
