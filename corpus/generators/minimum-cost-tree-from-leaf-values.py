import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        arr = [rng.randint(1, 15) for _ in range(rng.randint(2, 40))]
        key = tuple(arr)
        if key not in seen:
            seen.add(key)
            assert 2 <= len(arr) <= 40 and all(1 <= v <= 15 for v in arr)
            cases.append(f"candidate(arr={arr!r})")
    return cases
