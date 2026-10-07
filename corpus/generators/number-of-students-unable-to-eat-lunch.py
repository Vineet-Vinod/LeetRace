import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], tuple[int, ...]]] = {
        ((1, 1, 0, 0), (0, 1, 0, 1)),
        ((1, 1, 1, 0, 0, 1), (1, 0, 0, 0, 1, 1)),
    }
    cases.add(((0, 1) * 50, (1, 0) * 50))
    while len(cases) < 600:
        size = rng.randint(1, 100)
        students = tuple(rng.randrange(2) for _ in range(size))
        sandwiches = tuple(rng.randrange(2) for _ in range(size))
        cases.add((students, sandwiches))
    return [
        f"candidate(students={list(students)!r}, sandwiches={list(sandwiches)!r})"
        for students, sandwiches in cases
    ]
