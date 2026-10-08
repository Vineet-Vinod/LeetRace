import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty binary grids within the 1000-by-1000 limit."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        m = 1 + i % 20
        n = 1 + (i * 7) % 20
        grid = [[rng.randrange(2) for _ in range(n)] for _ in range(m)]
        call = f"candidate(grid={grid!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
