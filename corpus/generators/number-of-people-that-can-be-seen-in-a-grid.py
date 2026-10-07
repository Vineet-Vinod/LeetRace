import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    grids = {
        ((3, 1, 4, 2, 5),),
        ((5, 1), (3, 1), (4, 1)),
        ((1,),),
        ((100000,),),
        tuple(tuple(r + c + 1 for c in range(400)) for r in range(400)),
    }
    while len(grids) < 600:
        rows, cols = rng.randint(1, 16), rng.randint(1, 16)
        ceiling = rng.choice((20, 100000))
        grids.add(
            tuple(
                tuple(rng.randint(1, ceiling) for _ in range(cols)) for _ in range(rows)
            )
        )
    assert len(grids) == 600
    assert all(
        1 <= len(g) <= 400
        and 1 <= len(g[0]) <= 400
        and all(
            len(row) == len(g[0]) and all(1 <= h <= 100000 for h in row) for row in g
        )
        for g in grids
    )
    return [
        f"candidate(heights={[[x for x in row] for row in g]!r})" for g in sorted(grids)
    ]
