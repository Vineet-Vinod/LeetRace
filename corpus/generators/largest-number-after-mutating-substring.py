import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[str, tuple[int, ...]]] = {
        ("132", (9, 8, 5, 0, 3, 6, 4, 2, 6, 8)),
        ("021", (9, 4, 3, 5, 7, 2, 1, 9, 0, 6)),
        ("5", (1, 4, 7, 5, 3, 2, 5, 6, 9, 4)),
        ("0" * 1000, tuple(range(10))),
    }
    cases.add(("0" * 100_000, tuple(range(10))))
    digits = "0123456789"
    while len(cases) < 600:
        num = "".join(rng.choice(digits) for _ in range(rng.randint(1, 80)))
        change = tuple(rng.randint(0, 9) for _ in range(10))
        cases.add((num, change))
    assert all(
        1 <= len(num) <= 100_000
        and set(num) <= set(digits)
        and len(change) == 10
        and all(0 <= value <= 9 for value in change)
        for num, change in cases
    )
    return [
        f"candidate(num={num!r}, change={list(change)!r})"
        for num, change in sorted(cases)
    ]
