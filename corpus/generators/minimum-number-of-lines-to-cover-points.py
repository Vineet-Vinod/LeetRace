import random


def generate(seed: int = 0) -> list[str]:
    """Generate 600 distinct sets of 1..10 unique integer points."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 1 + i % 10
        points = []
        while len(points) < n:
            point = [rng.randrange(-100, 101), rng.randrange(-100, 101)]
            if point not in points:
                points.append(point)
        call = f"candidate(points={points!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
