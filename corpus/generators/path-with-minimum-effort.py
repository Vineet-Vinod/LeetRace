import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty rectangular height grids with values in [1,10^6]."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        rows = 1 + i % 12
        cols = 1 + (i * 7) % 12
        heights = [
            [rng.randrange(1, 10**6 + 1) for _ in range(cols)] for _ in range(rows)
        ]
        call = f"candidate(heights={heights!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
