import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    fixed = [(2.0, 10), (2.0, -2), (0.0, 1), (-2.0, 3), (1.5, 0)]
    for x, n in fixed:
        cases.append(f"candidate(x={x!r}, n={n})")
        seen.add((x, n))
    while len(cases) < 600:
        x = round(rng.uniform(-2, 2), 3)
        if x == 0 and rng.random() < 0.5:
            x = 0.5
        n = rng.randint(-10, 10)
        if (x, n) not in seen and not (x == 0 and n <= 0):
            seen.add((x, n))
            assert (
                -100.0 < x < 100.0 and -(2**31) <= n <= 2**31 - 1 and (x != 0 or n > 0)
            )
            cases.append(f"candidate(x={x!r}, n={n})")
    return cases
