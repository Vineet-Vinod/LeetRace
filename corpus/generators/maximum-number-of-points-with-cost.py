import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty rectangular nonnegative point matrices."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        rows = 1 + i % 10
        cols = 1 + (i * 7) % 10
        points = [[rng.randrange(0, 101) for _ in range(cols)] for _ in range(rows)]
        call = f"candidate(points={points!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
