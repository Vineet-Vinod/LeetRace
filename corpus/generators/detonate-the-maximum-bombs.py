import random


def generate(seed: int = 0) -> list[str]:
    """Use unique in-bounds bomb coordinates and legal positive radii."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    index = 0
    while len(calls) < 600:
        count = 1 + index % 30
        points = rng.sample(range(1, 100_001), count * 2)
        bombs = [
            [points[offset], points[offset + 1], rng.randint(1, 100_000)]
            for offset in range(0, count * 2, 2)
        ]
        assert 1 <= len(bombs) <= 100
        assert len({(x, y) for x, y, _ in bombs}) == len(bombs)
        assert all(
            1 <= x <= 100_000 and 1 <= y <= 100_000 and 1 <= radius <= 100_000
            for x, y, radius in bombs
        )
        call = f"candidate(bombs={bombs!r})"
        index += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
