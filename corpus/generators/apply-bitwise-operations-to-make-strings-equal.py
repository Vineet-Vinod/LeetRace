import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[str, str]] = {
        ("1010", "0110"),
        ("11", "00"),
        ("00", "00"),
        ("1" + "0" * 99_999, "0" * 99_999 + "1"),
        ("0" * 100_000, "0" * 100_000),
        ("0" * 100_000, "0" * 99_999 + "1"),
    }
    while len(cases) < 600:
        size = rng.randint(2, 100)
        mode = rng.randrange(3)
        if mode == 0:
            source = "".join(rng.choice("01") for _ in range(size))
            target = "".join(rng.choice("01") for _ in range(size))
        elif mode == 1:
            source = "0" * size
            target = "0" * (size - 1) + "1"
        else:
            source = "0" * (size - 1) + "1"
            target = "1" + "0" * (size - 1)
        cases.add((source, target))
    assert all(
        2 <= len(source) == len(target) <= 100_000
        and set(source) <= set("01")
        and set(target) <= set("01")
        for source, target in cases
    )
    return [
        f"candidate(s={source!r}, target={target!r})"
        for source, target in sorted(cases)
    ]
