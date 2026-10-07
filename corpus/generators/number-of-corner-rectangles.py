import random


def generate(seed: int = 0) -> list[str]:
    """Generate binary grids with 1..6000 one-cells and rectangular dimensions."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        m = 1 + i % 20
        n = 1 + (i * 7) % 20
        grid = [[rng.randrange(2) for _ in range(n)] for _ in range(m)]
        if not any(map(any, grid)):
            grid[0][0] = 1
        call = f"candidate(grid={grid!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
