import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = []
    seen = set()
    while len(cases) < 600:
        k = rng.randint(2, 8)
        n = rng.randint(k, 8)
        cookies = [rng.randint(1, 10**5) for _ in range(n)]
        key = (tuple(cookies), k)
        if key not in seen:
            seen.add(key)
            assert 2 <= k <= len(cookies) <= 8 and all(1 <= v <= 10**5 for v in cookies)
            cases.append(f"candidate(cookies={cookies!r}, k={k})")
    return cases
