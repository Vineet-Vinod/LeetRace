import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        ((10, 20), (30, 200), (400, 50), (30, 20)),
        ((259, 770), (448, 54), (926, 667), (184, 139), (840, 118), (577, 469)),
    }
    while len(cases) < 600:
        n = 2 * rng.randint(1, 50)
        cases.add(tuple((rng.randint(1, 1000), rng.randint(1, 1000)) for _ in range(n)))
    return [f"candidate(costs={[list(pair) for pair in costs]!r})" for costs in cases]
