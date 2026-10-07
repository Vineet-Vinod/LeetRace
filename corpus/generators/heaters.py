import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        houses = [rng.randint(1, 10**9) for _ in range(rng.randint(1, 60))]
        heaters = [rng.randint(1, 10**9) for _ in range(rng.randint(1, 30))]
        key = (tuple(houses), tuple(heaters))
        if key not in seen:
            seen.add(key)
            assert houses and heaters and all(1 <= x <= 10**9 for x in houses + heaters)
            cases.append(f"candidate(houses={houses!r}, heaters={heaters!r})")
    return cases
