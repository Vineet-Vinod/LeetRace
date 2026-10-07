import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[str, ...]] = {
        ("011001", "000000", "010100", "001000"),
        ("000", "111", "000"),
        ("0",),
        ("1",),
        tuple("1" * 500 for _ in range(500)),
    }
    while len(cases) < 600:
        rows, cols = rng.randint(1, 20), rng.randint(1, 20)
        cases.add(
            tuple("".join(rng.choice("01") for _ in range(cols)) for _ in range(rows))
        )
    assert all(
        1 <= len(bank) <= 500
        and 1 <= len(bank[0]) <= 500
        and all(len(row) == len(bank[0]) and set(row) <= {"0", "1"} for row in bank)
        for bank in cases
    )
    return [f"candidate(bank={list(bank)!r})" for bank in sorted(cases)]
