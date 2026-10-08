import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[int, ...]] = {(1,), (1, 1, 4, 2, 1, 3), (5, 1, 2, 3, 4)}
    cases.add((100,) * 100)
    while len(cases) < 600:
        cases.add(tuple(rng.randint(1, 100) for _ in range(rng.randint(1, 100))))
    calls = [f"candidate(heights={list(values)!r})" for values in cases]
    calls.extend(["candidate(heights=[1, 2, 3, 4, 5])"])
    return list(dict.fromkeys(calls))
