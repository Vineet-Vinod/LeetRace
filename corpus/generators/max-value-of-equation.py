import random

EXAMPLES = [
    "candidate(points=[[1, 3], [2, 0], [5, 10], [6, -10]], k=1)",
    "candidate(points=[[0, 0], [3, 0], [9, 2]], k=3)",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(points, k):
        assert 2 <= len(points) <= 100000 and 0 <= k <= 2 * 10**8
        assert all(
            len(p) == 2 and all(-(10**8) <= v <= 10**8 for v in p) for p in points
        )
        assert all(a[0] < b[0] for a, b in zip(points, points[1:]))
        assert any(b[0] - a[0] <= k for a, b in zip(points, points[1:]))
        emit(f"candidate(points={points!r}, k={k})")

    add([[i, 10**8 if i % 2 else -(10**8)] for i in range(100000)], 2 * 10**8)
    add([[-(10**8), -(10**8)], [10**8, 10**8]], 2 * 10**8)
    while len(calls) < 600:
        xs = sorted(rng.sample(range(-1000, 1001), rng.randint(2, 40)))
        negative = rng.random() < 0.3
        points = [
            [x, rng.randint(-10000, -2000) if negative else rng.randint(-10000, 10000)]
            for x in xs
        ]
        minimum = min(b - a for a, b in zip(xs, xs[1:]))
        add(points, rng.randint(minimum, 2000))
    return calls
