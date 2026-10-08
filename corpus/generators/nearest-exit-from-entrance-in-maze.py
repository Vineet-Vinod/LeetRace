import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[str, ...], tuple[int, int]]] = {
        (("+.+", "...", "+.+"), (1, 1)),
        ((".+", ".."), (0, 0)),
        (("..",), (0, 0)),
        ((".+",), (0, 0)),
    }
    cases.add((tuple("." * 100 for _ in range(100)), (50, 50)))
    while len(cases) < 600:
        rows, cols = rng.randint(1, 15), rng.randint(1, 15)
        maze = [
            list("." if rng.random() < 0.65 else "+" for _ in range(cols))
            for _ in range(rows)
        ]
        entrance = (rng.randrange(rows), rng.randrange(cols))
        maze[entrance[0]][entrance[1]] = "."
        cases.add((tuple("".join(row) for row in maze), entrance))
    assert all(
        1 <= len(maze) <= 100
        and 1 <= len(maze[0]) <= 100
        and all(len(row) == len(maze[0]) and set(row) <= {".", "+"} for row in maze)
        and 0 <= entrance[0] < len(maze)
        and 0 <= entrance[1] < len(maze[0])
        and maze[entrance[0]][entrance[1]] == "."
        for maze, entrance in cases
    )
    return [
        f"candidate(maze={[list(row) for row in maze]!r}, entrance={list(entrance)!r})"
        for maze, entrance in sorted(cases)
    ]
