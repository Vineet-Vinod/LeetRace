import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    fixed = [(1, 1), (5, 4), (3, 3), (10, 7), (1, 10**9)]
    for n, target in fixed:
        key = (n, target)
        seen.add(key)
        cases.append(f"candidate(n={n}, target={target})")
    while len(cases) < 600:
        n = rng.randint(1, 1000)
        target = rng.randint(1, 10**9)
        key = (n, target)
        if key not in seen:
            seen.add(key)
            assert n >= 1 and target >= 1
            cases.append(f"candidate(n={n}, target={target})")
    return cases
