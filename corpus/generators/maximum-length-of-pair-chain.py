import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        pairs = []
        for _ in range(rng.randint(1, 40)):
            left = rng.randint(-1000, 999)
            right = rng.randint(left + 1, 1000)
            pairs.append([left, right])
        key = tuple(map(tuple, pairs))
        if key not in seen:
            seen.add(key)
            assert all(-1000 <= a < b <= 1000 for a, b in pairs)
            cases.append(f"candidate(pairs={pairs!r})")
    return cases
