import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(30, 20, 150, 100, 40), (60, 60, 60)}
    while len(cases) < 600:
        cases.add(tuple(rng.randint(1, 500) for _ in range(rng.randint(1, 100))))
    return [f"candidate(time={list(values)!r})" for values in cases]
