import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[str, ...], tuple[int, ...]]] = {
        (("G", "P", "GP", "GG"), (2, 4, 3)),
        (("MMM", "PGM", "GP"), (3, 10)),
        (("M", "P"), (1,)),
    }
    cases.add((tuple("M" for _ in range(100_000)), tuple(1 for _ in range(99_999))))
    while len(cases) < 600:
        houses = tuple(
            "".join(rng.choice("MPG") for _ in range(rng.randint(1, 10)))
            for _ in range(rng.randint(2, 50))
        )
        travel = tuple(rng.randint(1, 100) for _ in range(len(houses) - 1))
        cases.add((houses, travel))
    assert all(
        2 <= len(houses) <= 100_000
        and len(travel) == len(houses) - 1
        and all(1 <= len(house) <= 10 and set(house) <= set("MPG") for house in houses)
        and all(1 <= time <= 100 for time in travel)
        for houses, travel in cases
    )
    return [
        f"candidate(garbage={list(houses)!r}, travel={list(travel)!r})"
        for houses, travel in sorted(cases)
    ]
