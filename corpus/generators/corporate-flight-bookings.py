import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases, seen = [], set()
    while len(cases) < 600:
        n = rng.randint(1, 80)
        bookings = []
        for _ in range(rng.randint(1, 60)):
            first = rng.randint(1, n)
            last = rng.randint(first, n)
            bookings.append([first, last, rng.randint(1, 10000)])
        key = (n, tuple(map(tuple, bookings)))
        if key not in seen:
            seen.add(key)
            assert all(1 <= a <= b <= n and seats >= 1 for a, b, seats in bookings)
            cases.append(f"candidate(bookings={bookings!r}, n={n})")
    return cases
