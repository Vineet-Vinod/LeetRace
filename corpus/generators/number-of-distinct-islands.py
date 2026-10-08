import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    grids = {
        ((1, 1, 0, 0, 0), (1, 1, 0, 0, 0), (0, 0, 0, 1, 1), (0, 0, 0, 1, 1)),
        ((1, 1, 0, 1, 1), (1, 0, 0, 0, 0), (0, 0, 0, 0, 1), (1, 1, 0, 1, 1)),
        ((0,),),
        ((1,),),
        tuple(tuple(int(r == 0 or c == 0) for c in range(50)) for r in range(50)),
    }
    while len(grids) < 600:
        rows, cols = rng.randint(1, 14), rng.randint(1, 14)
        density = rng.choice((0.12, 0.3, 0.5, 0.72))
        grids.add(
            tuple(
                tuple(int(rng.random() < density) for _ in range(cols))
                for _ in range(rows)
            )
        )
    assert len(grids) == 600
    assert all(
        1 <= len(g) <= 50
        and 1 <= len(g[0]) <= 50
        and all(len(row) == len(g[0]) and all(x in (0, 1) for x in row) for row in g)
        for g in grids
    )
    return [
        f"candidate(grid={[[x for x in row] for row in g]!r})" for g in sorted(grids)
    ]
