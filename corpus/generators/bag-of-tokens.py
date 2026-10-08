import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int]] = {
        ((), 0),
        ((100,), 99),
        ((100,), 100),
        ((100, 200, 300, 400), 200),
        ((0, 0, 1), 0),
        ((9999, 9999), 9999),
        (tuple(range(1000)), 0),
    }
    while len(cases) < 600:
        size = rng.randint(0, 35)
        tokens = tuple(rng.randint(0, 9999) for _ in range(size))
        cases.add((tokens, rng.randint(0, 9999)))
    assert all(
        len(tokens) <= 1000
        and 0 <= power < 10_000
        and all(0 <= token < 10_000 for token in tokens)
        for tokens, power in cases
    )
    return [
        f"candidate(tokens={list(tokens)!r}, power={power})"
        for tokens, power in sorted(cases)
    ]
