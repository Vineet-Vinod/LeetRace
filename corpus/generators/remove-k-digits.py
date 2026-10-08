import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[str, int]] = {
        ("1432219", 3),
        ("10200", 1),
        ("10", 2),
        ("9", 1),
        ("1000", 1),
        ("9" * 100_000, 100_000),
        ("123", 1),
    }
    while len(cases) < 600:
        size = rng.randint(1, 100)
        first = rng.choice("123456789")
        num = first + "".join(rng.choice("0123456789") for _ in range(size - 1))
        cases.add((num, rng.randint(1, size)))
    assert all(
        1 <= len(num) <= 100_000
        and 1 <= k <= len(num)
        and num.isdigit()
        and (num == "0" or num[0] != "0")
        for num, k in cases
    )
    return [f"candidate(num={num!r}, k={k})" for num, k in sorted(cases)]
