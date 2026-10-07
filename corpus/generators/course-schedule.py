import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(2, ((1, 0),)), (2, ((1, 0), (0, 1))), (1, ())}
    while len(cases) < 600:
        n = rng.randint(1, 60)
        possible = [
            (course, pre) for course in range(n) for pre in range(n) if course != pre
        ]
        edges = tuple(
            sorted(rng.sample(possible, rng.randint(0, min(120, len(possible)))))
        )
        cases.add((n, edges))
    return [
        f"candidate(numCourses={n}, prerequisites={[list(edge) for edge in edges]!r})"
        for n, edges in cases
    ]
