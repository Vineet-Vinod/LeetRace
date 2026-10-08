import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        lo = rng.randint(1, 1000)
        hi = rng.randint(lo, min(1000, lo + 100))
        k = rng.randint(1, hi - lo + 1)
        key = (lo, hi, k)
        if key not in seen:
            seen.add(key)
            assert 1 <= lo <= hi <= 1000 and 1 <= k <= hi - lo + 1
            cases.append(f"candidate(lo={lo}, hi={hi}, k={k})")
    return cases
