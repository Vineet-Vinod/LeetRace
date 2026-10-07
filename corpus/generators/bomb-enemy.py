import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[str, ...], ...]] = {
        (("0",),),
        (("E",),),
        (("W",),),
        (("0", "E", "0"), ("E", "0", "W"), ("0", "E", "0")),
    }
    while len(cases) < 600:
        rows, cols = rng.randint(1, 20), rng.randint(1, 20)
        cases.add(
            tuple(tuple(rng.choice("WE0") for _ in range(cols)) for _ in range(rows))
        )
    return [f"candidate(grid={[list(row) for row in grid]!r})" for grid in cases]
