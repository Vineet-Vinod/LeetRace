import random

EXAMPLES = [
    "candidate(points=[[1, 1], [6, 1]], k=2)",
    "candidate(points=[[3, 3], [1, 2], [9, 2]], k=2)",
    "candidate(points=[[3, 3], [1, 2], [9, 2]], k=3)",
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
        assert 2 <= len(points) <= 50 and 2 <= k <= len(points)
        assert all(len(p) == 2 and all(1 <= v <= 100 for v in p) for p in points)
        emit(f"candidate(points={points!r}, k={k})")

    add([[1, 1], [100, 100]], 2)
    add([[1, 1], [1, 100], [100, 1], [100, 100]] * 12 + [[50, 50], [51, 51]], 50)
    add([[100, 100]] * 50, 50)
    add([[1, 1], [1, 2], [2, 1], [2, 2]], 4)
    while len(calls) < 600:
        n = rng.randint(2, 20)
        points = [[rng.randint(1, 100), rng.randint(1, 100)] for _ in range(n)]
        if rng.random() < 0.3:
            center = [rng.randint(1, 100), rng.randint(1, 100)]
            points = [center[:]] * rng.randint(2, n) + points
            points = points[:n]
        if rng.random() < 0.2:
            points = [[rng.randint(1, 100), 50] for _ in range(n)]
        add(points, rng.randint(2, n))
    return calls
