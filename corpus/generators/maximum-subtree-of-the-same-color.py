import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[tuple[int, int], ...], tuple[int, ...]]] = {
        (((0, 1), (0, 2), (0, 3)), (1, 1, 2, 3)),
        (((0, 1), (0, 2), (0, 3)), (1, 1, 1, 1)),
        (((0, 1), (0, 2), (2, 3), (2, 4)), (1, 2, 3, 3, 3)),
        (tuple((0, node) for node in range(1, 50_000)), (7,) * 50_000),
        (tuple((0, node) for node in range(1, 50_000)), (10**5,) * 50_000),
    }
    while len(cases) < 600:
        n = rng.randint(1, 100)
        edges = tuple((rng.randrange(node), node) for node in range(1, n))
        mode = rng.randrange(3)
        if mode == 0:
            colors = (rng.randint(1, 10**5),) * n
        elif mode == 1:
            colors = tuple(rng.randint(1, 4) for _ in range(n))
        else:
            colors = tuple(rng.randint(1, 10**5) for _ in range(n))
        cases.add((edges, colors))
    assert all(
        1 <= len(colors) <= 50_000
        and len(edges) == len(colors) - 1
        and all(
            0 <= a < len(colors) and 0 <= b < len(colors) and a != b for a, b in edges
        )
        and 1 <= min(colors) <= max(colors) <= 10**5
        for edges, colors in cases
    )
    return [
        f"candidate(edges={[list(edge) for edge in edges]!r}, colors={list(colors)!r})"
        for edges, colors in sorted(cases)
    ]
