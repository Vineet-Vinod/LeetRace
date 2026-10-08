import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    example = (
        (0, 0, 1, 0, 0),
        (0, 0, 0, 0, 0),
        (0, 0, 0, 1, 0),
        (1, 1, 0, 1, 1),
        (0, 0, 0, 0, 0),
    )
    cases = {(example, (0, 4), (4, 4)), (example, (0, 4), (3, 2))}
    while len(cases) < 600:
        rows, cols = rng.randint(2, 15), rng.randint(2, 15)
        maze = [[rng.randint(0, 1) for _ in range(cols)] for _ in range(rows)]
        start = (rng.randrange(rows), rng.randrange(cols))
        destination = (rng.randrange(rows), rng.randrange(cols))
        maze[start[0]][start[1]] = 0
        maze[destination[0]][destination[1]] = 0
        if (
            start != destination
            and sum(value == 0 for row in maze for value in row) >= 2
        ):
            cases.add((tuple(tuple(row) for row in maze), start, destination))
    return [
        f"candidate(maze={[list(row) for row in maze]!r}, start={list(start)!r}, destination={list(destination)!r})"
        for maze, start, destination in cases
    ]
