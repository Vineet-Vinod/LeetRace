import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases, seen = [], set()
    while len(cases) < 600:
        hours = [rng.randint(1, 10**9) for _ in range(rng.randint(1, 100))]
        key = tuple(hours)
        if key not in seen:
            seen.add(key)
            assert 1 <= len(hours) <= 100000 and all(1 <= h <= 10**9 for h in hours)
            cases.append(f"candidate(hours={hours!r})")
    return cases
