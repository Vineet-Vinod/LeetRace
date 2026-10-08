import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {(1, 1), (10, 3), (5, 6), (1000, 1)}
    cases.add((1000, 1000))
    while len(cases) < 600:
        cases.add((rng.randint(1, 1000), rng.randint(1, 1000)))
    calls = [f"candidate(n={n}, m={m})" for n, m in cases]
    calls.extend(["candidate(n=5, m=1)"])
    return list(dict.fromkeys(calls))
