import random


def make_mountain(rng: random.Random) -> tuple[int, ...]:
    size = rng.randint(3, 200)
    values = sorted(rng.sample(range(0, 10_001), size))
    peak = rng.randint(1, size - 2)
    return tuple(values[: peak + 1] + list(reversed(values[peak + 1 :])))


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {
        (2, 1),
        (3, 5, 5),
        (0, 3, 2, 1),
        tuple(range(5001)) + tuple(range(4999, 0, -1)),
        (0, 10_000, 0),
    }
    while len(cases) < 600:
        cases.add(tuple(rng.randint(0, 10_000) for _ in range(rng.randint(1, 200))))
        cases.add(make_mountain(rng))
    return [f"candidate(arr={list(values)!r})" for values in cases]
