import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], int, int]] = {
        ((2, 2, 3, 3), 5, 5),
        ((2, 2, 3, 3), 3, 4),
        ((5,), 10, 8),
        ((1,), 1, 1),
        ((10**6,) * 10, 10**6, 10**6),
        ((10**6,) * 100_000, 10**9, 10**9),
    }
    while len(cases) < 600:
        n = rng.randint(1, 100)
        plants = tuple(rng.randint(1, 1000) for _ in range(n))
        cap_a = rng.randint(max(plants), max(plants) + 10_000)
        cap_b = rng.randint(max(plants), max(plants) + 10_000)
        cases.add((plants, cap_a, cap_b))
    assert all(
        1 <= len(plants) <= 100_000
        and all(1 <= x <= 10**6 for x in plants)
        and max(plants) <= a <= 10**9
        and max(plants) <= b <= 10**9
        for plants, a, b in cases
    )
    return [
        f"candidate(plants={list(plants)!r}, capacityA={a}, capacityB={b})"
        for plants, a, b in sorted(cases)
    ]
