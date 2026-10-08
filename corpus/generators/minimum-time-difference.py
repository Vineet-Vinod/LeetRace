import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {("23:59", "00:00"), ("00:00", "23:59", "00:00")}
    while len(cases) < 600:
        points = tuple(
            f"{rng.randrange(24):02d}:{rng.randrange(60):02d}"
            for _ in range(rng.randint(2, 30))
        )
        cases.add(points)
    return [f"candidate(timePoints={list(points)!r})" for points in cases]
