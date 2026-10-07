import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases, seen = [], set()
    while len(cases) < 600:
        lights = [
            [rng.randint(-1000, 1000), rng.randint(0, 100)]
            for _ in range(rng.randint(1, 20))
        ]
        key = tuple(map(tuple, lights))
        if key not in seen:
            seen.add(key)
            assert all(-(10**8) <= p <= 10**8 and 0 <= r <= 10**8 for p, r in lights)
            cases.append(f"candidate(lights={lights!r})")
    return cases
