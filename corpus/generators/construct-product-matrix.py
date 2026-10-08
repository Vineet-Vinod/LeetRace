import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty rectangular grids with legal positive values and bounded dimensions."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        rows = 1 + i % 8
        cols = 1 + (i * 5) % 8
        grid = [[rng.randrange(1, 10001) for _ in range(cols)] for _ in range(rows)]
        assert all(len(row) == cols for row in grid) and all(
            1 <= x <= 10**4 for row in grid for x in row
        )
        call = f"candidate(grid={grid!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
