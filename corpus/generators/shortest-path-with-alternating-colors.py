import random


def generate(seed: int = 0) -> list[str]:
    """Generate directed colored edges with endpoints in [0,n), allowing duplicates as permitted."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 1 + i % 20
        red = [[rng.randrange(n), rng.randrange(n)] for _ in range(i % 30)]
        blue = [[rng.randrange(n), rng.randrange(n)] for _ in range((i * 7) % 30)]
        call = f"candidate(n={n}, redEdges={red!r}, blueEdges={blue!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
