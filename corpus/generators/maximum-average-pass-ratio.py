import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[tuple[int, int], ...], int]] = {
        (((1, 2), (3, 5), (2, 2)), 2),
        (((2, 4), (3, 9), (4, 5), (2, 10)), 4),
        (((1, 1),), 1),
    }
    cases.add((((1, 1),) * 100_000, 100_000))
    while len(cases) < 600:
        classes = []
        for _ in range(rng.randint(1, 30)):
            total = rng.randint(1, 100_000)
            classes.append((rng.randint(1, total), total))
        cases.add((tuple(classes), rng.randint(1, 100)))
    assert all(
        1 <= len(classes) <= 100_000
        and 1 <= extra <= 100_000
        and all(1 <= passed <= total <= 100_000 for passed, total in classes)
        for classes, extra in cases
    )
    return [
        f"candidate(classes={[list(pair) for pair in classes]!r}, extraStudents={extra})"
        for classes, extra in sorted(cases)
    ]
