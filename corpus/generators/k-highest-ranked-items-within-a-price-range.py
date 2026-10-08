import random


def generate(seed: int = 0) -> list[str]:
    """Grid has at least one nonwall start; pricing is ordered and k is positive."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        m = 1 + i % 8
        n = 1 + (i * 7) % 8
        grid = [[rng.randrange(0, 12) for _ in range(n)] for _ in range(m)]
        sr = rng.randrange(m)
        sc = rng.randrange(n)
        grid[sr][sc] = max(1, grid[sr][sc])
        low = rng.randrange(1, 12)
        high = rng.randrange(low, 13)
        k = 1 + i % (m * n)
        call = f"candidate(grid={grid!r}, pricing={[low, high]!r}, start={[sr, sc]!r}, k={k})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
