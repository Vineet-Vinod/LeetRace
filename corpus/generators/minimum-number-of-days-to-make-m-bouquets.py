import random


def generate(seed: int = 0) -> list[str]:
    r = random.Random(seed)
    cases = []
    seen = set()

    def add(days, m, k):
        key = (tuple(days), m, k)
        if key not in seen:
            assert 1 <= len(days) <= 100_000 and all(1 <= x <= 10**9 for x in days)
            assert 1 <= m <= 10**6 and 1 <= k <= len(days)
            seen.add(key)
            cases.append(f"candidate(bloomDay={days!r}, m={m}, k={k})")

    for _ in range(300):
        n = r.randint(1, 100)
        k = r.randint(1, n)
        m = r.randint(1, n // k)
        days = [r.randint(1, 1000) for _ in range(n)]
        add(days, m, k)
    for _ in range(300):
        n = r.randint(1, 100)
        k = r.randint(1, n)
        m = n // k + 1
        days = [r.randint(1, 1000) for _ in range(n)]
        add(days, m, k)
    days = list(range(1, 100001))
    add(days, 1000, 100)
    add(days, 1001, 100)
    return cases
