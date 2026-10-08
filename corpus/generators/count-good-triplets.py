import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int, int, int]] = {
        ((0, 0, 0), 0, 0, 0),
        ((3, 0, 1, 1, 9, 7), 7, 2, 3),
    }
    cases.add((tuple([0, 1000] * 50), 0, 0, 0))
    cases.add((tuple([0, 1000] * 50), 1000, 1000, 1000))
    while len(cases) < 600:
        size = rng.randint(3, 100)
        arr = tuple(rng.randint(0, 1000) for _ in range(size))
        cases.add(
            (arr, rng.randint(0, 1000), rng.randint(0, 1000), rng.randint(0, 1000))
        )
    calls = [f"candidate(arr={list(a)!r}, a={x}, b={y}, c={z})" for a, x, y, z in cases]
    calls.extend(["candidate(arr=[1, 1, 2, 2, 3], a=0, b=0, c=1)"])
    return list(dict.fromkeys(calls))
