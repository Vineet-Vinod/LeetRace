import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    rows = 50000
    grids = {
        (tuple([1] * rows), tuple([1] * rows)),
        (tuple(range(1, rows + 1)), tuple(reversed(range(1, rows + 1)))),
    }
    while len(grids) < 600:
        width = rng.randint(1, 80)
        grid = (
            tuple(rng.randint(1, 100000) for _ in range(width)),
            tuple(rng.randint(1, 100000) for _ in range(width)),
        )
        grids.add(grid)
    cases = [f"candidate(grid={[list(top), list(bottom)]!r})" for top, bottom in grids]
    assert len(cases) == len(set(cases)) == 600
    assert all(
        1 <= len(top) == len(bottom) <= 50000
        and min(top) >= 1
        and max(top) <= 100000
        and min(bottom) >= 1
        and max(bottom) <= 100000
        for top, bottom in grids
    )
    return cases
