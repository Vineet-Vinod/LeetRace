import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, tuple[tuple[int, int], ...]]] = {
        (3, ((1, 2), (1, 3), (1, 8), (2, 6))),
        (2, ((2, 1), (1, 8), (2, 6))),
        (4, ((4, 3), (1, 4), (4, 6), (1, 7))),
    }
    cases.add((1_000_000_000, ((1, 1),)))
    while len(cases) < 600:
        rows = rng.randint(1, 100)
        occupied = set()
        for _ in range(rng.randint(1, min(rows * 10, 100))):
            occupied.add((rng.randint(1, rows), rng.randint(1, 10)))
        cases.add((rows, tuple(sorted(occupied))))
    assert all(
        1 <= rows <= 10**9
        and 1 <= len(reserved) <= min(10 * rows, 10_000)
        and len(set(reserved)) == len(reserved)
        and all(1 <= row <= rows and 1 <= seat <= 10 for row, seat in reserved)
        for rows, reserved in cases
    )
    return [
        f"candidate(n={rows}, reservedSeats={[[r, s] for r, s in reserved]!r})"
        for rows, reserved in sorted(cases)
    ]
