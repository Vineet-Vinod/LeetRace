import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[str, tuple[tuple[int, int, int], ...]]] = {
        ("abc", ((0, 1, 0), (1, 2, 1), (0, 2, 1))),
        ("dztz", ((0, 0, 0), (1, 1, 1))),
        ("a", ((0, 0, 1),)),
        ("a" * 50_000, ((0, 49_999, 1),) * 50_000),
    }
    while len(cases) < 600:
        size = rng.randint(1, 80)
        s = "".join(rng.choice(string.ascii_lowercase) for _ in range(size))
        shifts = tuple(
            (
                start := rng.randrange(size),
                rng.randint(start, size - 1),
                rng.randint(0, 1),
            )
            for _ in range(rng.randint(1, 60))
        )
        cases.add((s, shifts))
    assert all(
        1 <= len(s) <= 50_000
        and 1 <= len(shifts) <= 50_000
        and all(
            0 <= start <= end < len(s) and direction in (0, 1)
            for start, end, direction in shifts
        )
        and set(s) <= set(string.ascii_lowercase)
        for s, shifts in cases
    )
    return [
        f"candidate(s={s!r}, shifts={[list(shift) for shift in shifts]!r})"
        for s, shifts in sorted(cases)
    ]
