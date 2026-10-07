import random


_MAX_ORIGINAL = 50_000
_MAX_VALUE = 100_000
_MAX_DIMENSION = 40_000


def generate(seed: int = 0) -> list[str]:
    """Every original array is nonempty; values and dimensions use the complete original bounds."""
    rng = random.Random(seed)
    cases = {
        ((1,), 1, 1),
        ((1, 2, 3, 4), 2, 2),
        ((1, 2, 3), 1, 3),
        ((1, 2), 1, 1),
        (tuple(range(1, _MAX_ORIGINAL + 1)), 200, 200),
        ((1,), _MAX_DIMENSION, 1),
        ((1,), 1, _MAX_DIMENSION),
        ((1,), _MAX_DIMENSION, _MAX_DIMENSION),
    }
    while len(cases) < 600:
        rows = rng.randint(1, 30)
        columns = rng.randint(1, 30)
        size = (
            rows * columns
            if rng.random() < 0.7
            else max(1, rows * columns + rng.choice((-2, -1, 1, 2)))
        )
        values = tuple(rng.randint(1, _MAX_VALUE) for _ in range(size))
        cases.add((values, rows, columns))

    assert len(cases) == 600
    assert all(1 <= len(values) <= _MAX_ORIGINAL for values, _, _ in cases)
    assert all(1 <= value <= _MAX_VALUE for values, _, _ in cases for value in values)
    assert all(
        1 <= rows <= _MAX_DIMENSION and 1 <= columns <= _MAX_DIMENSION
        for _, rows, columns in cases
    )
    return [
        f"candidate(original={list(values)!r}, m={rows}, n={columns})"
        for values, rows, columns in sorted(cases)
    ]
