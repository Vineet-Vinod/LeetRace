import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[str] = set()
    for i in range(600):
        rows = 4 + rng.randrange(8)
        cols = 4 + rng.randrange(8)
        maze = [
            [
                1 if r in (0, rows - 1) or c in (0, cols - 1) else rng.randrange(2)
                for c in range(cols)
            ]
            for r in range(rows)
        ]
        interior = [(r, c) for r in range(1, rows - 1) for c in range(1, cols - 1)]
        start, destination = rng.sample(interior, 2)
        maze[start[0]][start[1]] = maze[destination[0]][destination[1]] = 0
        if sum(cell == 0 for row in maze for cell in row) < 2:
            maze[interior[0][0]][interior[0][1]] = 0
        cases.add(
            f"candidate(maze={maze!r}, start={list(start)!r}, destination={list(destination)!r})"
        )
    return sorted(cases)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(maze=[[0, 0, 0], [0, 0, 0], [0, 0, 0]], start=[0, 0], destination=[1, 1])",
    "candidate(maze=[[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], start=[0, 4], destination=[4, 4])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
