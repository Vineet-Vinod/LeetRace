import random

EXAMPLES = [
    "candidate(forest=[[1, 2, 3], [0, 0, 4], [7, 6, 5]])",
    "candidate(forest=[[1, 2, 3], [0, 0, 0], [7, 6, 5]])",
    "candidate(forest=[[2, 3, 4], [0, 0, 5], [8, 7, 6]])",
]


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls = list(EXAMPLES)
    seen = set(calls)

    def emit(call: str) -> None:
        if call not in seen:
            calls.append(call)
            seen.add(call)

    def add(forest):
        assert 1 <= len(forest) <= 50 and 1 <= len(forest[0]) <= 50
        assert all(len(row) == len(forest[0]) for row in forest)
        values = [v for row in forest for v in row]
        assert all(0 <= v <= 10**9 for v in values)
        trees = [v for v in values if v > 1]
        assert trees and len(trees) == len(set(trees))
        emit(f"candidate(forest={forest!r})")

    large = [[1] * 50 for _ in range(50)]
    large[-1][-1] = 10**9
    add(large)
    large = [[r * 50 + c + 2 for c in range(50)] for r in range(50)]
    add(large)
    add([[0, 2]])
    add([[10**9]])
    while len(calls) < 600:
        rows, cols = rng.randint(1, 7), rng.randint(1, 7)
        forest = [
            [1 if rng.random() > 0.25 else 0 for _ in range(cols)] for _ in range(rows)
        ]
        spots = rng.sample(range(rows * cols), rng.randint(1, rows * cols))
        heights = rng.sample(range(2, 10000), len(spots))
        for pos, height in zip(spots, heights):
            forest[pos // cols][pos % cols] = height
        if rng.random() < 0.33:
            # Fully walkable instances give substantial reachable coverage.
            forest = [[v or 1 for v in row] for row in forest]
        add(forest)
    return calls
