import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(**kwargs):
        calls[
            "candidate(" + ", ".join(f"{k}={v!r}" for k, v in kwargs.items()) + ")"
        ] = None

    for fill in (0, 1):
        add(
            grid=[[fill] * 200 for _ in range(200)],
            hits=[[r, c] for r in range(200) for c in range(200)],
        )
    while len(calls) < 600:
        m, n = rng.randint(1, 10), rng.randint(1, 10)
        # Both stable and initially unsupported components are legal.
        grid = [
            [int(rng.random() < rng.choice((0.2, 0.6, 0.95))) for _ in range(n)]
            for _ in range(m)
        ]
        cells = [[r, c] for r in range(m) for c in range(n)]
        hits = rng.sample(cells, rng.randint(1, len(cells)))
        assert 1 <= len(hits) <= 40000 and len({tuple(x) for x in hits}) == len(hits)
        assert all(len(row) == n and all(x in (0, 1) for x in row) for row in grid)
        add(grid=grid, hits=hits)
    assert len(calls) == 600
    return list(calls)
