import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct building sets; each interval is nonempty and all bounds are valid."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    i = 0
    while len(calls) < 600:
        n = 1 + i % 18
        buildings = []
        for _ in range(n):
            left = rng.randrange(40)
            right = rng.randrange(left + 1, 50)
            buildings.append([left, right, rng.randrange(1, 40)])
        assert all(0 <= a < b <= 10**8 and 1 <= h <= 10**5 for a, b, h in buildings)
        call = f"candidate(buildings={buildings!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
