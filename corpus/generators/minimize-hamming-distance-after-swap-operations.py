import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[int, ...], tuple[int, ...], tuple[tuple[int, int], ...]]] = {
        ((1, 2, 3, 4), (2, 1, 4, 5), ((0, 1), (2, 3))),
        ((1, 2, 3, 4), (1, 3, 2, 4), ()),
        ((5, 1, 2, 4, 3), (1, 5, 4, 2, 3), ((0, 4), (4, 2), (1, 3), (1, 4))),
    }
    cases.add(
        (
            tuple(range(1, 100_001)),
            tuple(reversed(range(1, 100_001))),
            tuple((i, i + 1) for i in range(99_999)),
        )
    )
    while len(cases) < 600:
        size = rng.randint(1, 100)
        source = tuple(rng.randint(1, 100_000) for _ in range(size))
        target = tuple(rng.randint(1, 100_000) for _ in range(size))
        swaps = tuple(
            (first, second)
            for first, second in (
                tuple(sorted(rng.sample(range(size), 2)))
                for _ in range(rng.randint(0, min(100, size * (size - 1) // 2)))
            )
        )
        cases.add((source, target, swaps))
    assert all(
        1 <= len(source) <= 100_000
        and len(target) == len(source)
        and all(1 <= value <= 100_000 for value in source + target)
        and all(
            0 <= a < len(source) and 0 <= b < len(source) and a != b for a, b in swaps
        )
        for source, target, swaps in cases
    )
    return [
        f"candidate(source={list(source)!r}, target={list(target)!r}, allowedSwaps={[[a, b] for a, b in swaps]!r})"
        for source, target, swaps in sorted(cases)
    ]
