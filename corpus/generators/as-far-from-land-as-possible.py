import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], ...]] = {
        ((1,),),
        ((0,),),
        ((1, 0), (0, 1)),
        ((1, 0, 1), (0, 0, 0), (1, 0, 1)),
    }
    while len(cases) < 600:
        n = rng.randint(1, 15)
        cases.add(tuple(tuple(rng.randint(0, 1) for _ in range(n)) for _ in range(n)))
    return [f"candidate(grid={[list(row) for row in grid]!r})" for grid in cases]
