import random


def generate(seed: int = 0) -> list[str]:
    """Generate simple undirected highways, including zero and maximum toll boundaries."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    index = 0
    while len(calls) < 600:
        if index == 0:
            n = 1000
            highways = [[city, city + 1, 100_000] for city in range(n - 1)]
            discounts = 0
        else:
            n = 2 + index % 12
            roads: dict[tuple[int, int], int] = {}
            for a in range(n):
                for b in range(a + 1, n):
                    if rng.random() < 0.2:
                        roads[(a, b)] = rng.randrange(0, 100_001)
            if index % 2 == 0:
                for city in range(1, n):
                    roads.setdefault((city - 1, city), rng.randrange(0, 100_001))
            if not roads:
                roads[(0, 1)] = 0
            highways = [[a, b, toll] for (a, b), toll in sorted(roads.items())]
            discounts = 500 if index % 17 == 0 else index % 7
        assert 2 <= n <= 1000 and 1 <= len(highways) <= 1000
        assert len({(min(a, b), max(a, b)) for a, b, _ in highways}) == len(highways)
        assert all(
            0 <= a < n and 0 <= b < n and a != b and 0 <= toll <= 100_000
            for a, b, toll in highways
        )
        assert 0 <= discounts <= 500
        call = f"candidate(n={n}, highways={highways!r}, discounts={discounts})"
        index += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
