import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int]] = {
        ((2, 3, 5, 1, 3), 3),
        ((4, 2, 1, 1, 2), 1),
    }
    cases.add(((100,) * 100, 50))
    while len(cases) < 600:
        cases.add(
            (
                tuple(rng.randint(1, 100) for _ in range(rng.randint(2, 100))),
                rng.randint(1, 50),
            )
        )
    calls = [
        f"candidate(candies={list(values)!r}, extraCandies={extra})"
        for values, extra in cases
    ]
    calls.extend(["candidate(candies=[12, 1, 12], extraCandies=10)"])
    return list(dict.fromkeys(calls))
