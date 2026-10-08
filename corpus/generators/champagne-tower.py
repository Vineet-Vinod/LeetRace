import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, int, int]] = {
        (1, 1, 1),
        (2, 1, 1),
        (100_000_009, 33, 17),
        (0, 0, 0),
        (10**9, 99, 50),
    }
    while len(cases) < 600:
        row = rng.randint(0, 99)
        cases.add((rng.randint(0, 10**9), row, rng.randint(0, row)))
    assert all(
        0 <= poured <= 10**9 and 0 <= glass <= row < 100 for poured, row, glass in cases
    )
    return [
        f"candidate(poured={poured}, query_row={row}, query_glass={glass})"
        for poured, row, glass in sorted(cases)
    ]
