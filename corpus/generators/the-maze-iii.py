import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def emit(**values):
        maze, ball, hole = values["maze"], values["ball"], values["hole"]
        m, n = len(maze), len(maze[0])
        assert (
            1 <= m <= 100
            and 1 <= n <= 100
            and all(len(row) == n and all(x in (0, 1) for x in row) for row in maze)
        )
        assert (
            len(ball) == len(hole) == 2
            and ball != hole
            and all(
                0 <= p[0] < m and 0 <= p[1] < n and maze[p[0]][p[1]] == 0
                for p in [ball, hole]
            )
        )
        call = (
            "candidate("
            + ", ".join(name + "=" + repr(value) for name, value in values.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    emit(maze=[[0, 0]], ball=[0, 0], hole=[0, 1])
    emit(maze=[[0] * 100 for _ in range(100)], ball=[99, 99], hole=[0, 0])
    emit(maze=[[0] * 100 for _ in range(100)], ball=[99, 99], hole=[50, 50])
    emit(
        maze=[
            [0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [0, 1, 0, 0, 0],
        ],
        ball=[4, 3],
        hole=[0, 1],
    )
    while len(calls) < 600:
        m, n = rng.randint(1, 10), rng.randint(2, 10)
        maze = [[int(rng.random() < 0.3) for _ in range(n)] for _ in range(m)]
        ball, hole = rng.sample([(i, j) for i in range(m) for j in range(n)], 2)
        maze[ball[0]][ball[1]] = maze[hole[0]][hole[1]] = 0
        if rng.random() < 0.3:
            maze = [[0] * n for _ in range(m)]
            ball, hole = rng.sample([(i, j) for i in range(m) for j in range(n)], 2)
        emit(maze=maze, ball=list(ball), hole=list(hole))
    return calls
