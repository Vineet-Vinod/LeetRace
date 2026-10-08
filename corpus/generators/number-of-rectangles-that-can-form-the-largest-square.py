from __future__ import annotations

import random

DOMAIN_SIZE = None
EXAMPLE_CALLS = [
    "candidate(rectangles=[[5, 8], [3, 9], [5, 12], [16, 5]])",
    "candidate(rectangles=[[2, 3], [3, 7], [4, 3], [3, 7]])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set(EXAMPLE_CALLS)

    def add_rectangles(rectangles: list[list[int]]) -> None:
        assert 1 <= len(rectangles) <= 1000
        assert all(
            1 <= x <= 10**9 and 1 <= y <= 10**9 and x != y for x, y in rectangles
        )
        cases.add(f"candidate(rectangles={rectangles!r})")

    # These families force answers of 1, n, or an exact chosen tie count k.
    for n in range(1, 101):
        add_rectangles([[side, side + 1] for side in range(1, n + 1)])
        add_rectangles([[500, 500 + i] for i in range(1, n + 1)])
        if n > 1:
            k = 1 + (n * 37) % (n - 1)
            rectangles = [[500, 501 + i] for i in range(k)]
            rectangles.extend([[499, 600 + i] for i in range(n - k)])
            add_rectangles(rectangles)

    # Exercise maximum n and maximum dimensions with varied winning counts.
    add_rectangles([[10**9, 10**9 - 1] for _ in range(1000)])
    add_rectangles([[10**9, 10**9 - i] for i in range(1, 1001)])
    add_rectangles([[10**9, 10**9 - i] for i in range(1, 1000)] + [[10**9 - 1, 10**9]])

    while len(cases) < 600:
        n = rng.randint(2, 1000)
        k = rng.randint(1, n)
        pivot = rng.randint(2, 10**9 - 2000)
        rectangles = [[pivot, pivot + i] for i in range(1, k + 1)]
        rectangles.extend([[pivot - 1, pivot + 1000 + i] for i in range(n - k)])
        add_rectangles(rectangles)
    return sorted(cases)
