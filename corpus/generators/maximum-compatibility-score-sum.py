def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = set()
    while len(cases) < 600:
        m = rng.randint(1, 8)
        q = rng.randint(1, 8)
        students = [[rng.randrange(2) for _ in range(q)] for _ in range(m)]
        mentors = [[rng.randrange(2) for _ in range(q)] for _ in range(m)]
        cases.add(f"candidate(students={students!r},mentors={mentors!r})")
    return sorted(cases)
