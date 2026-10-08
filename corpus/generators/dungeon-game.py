import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        g = kwargs["dungeon"]
        assert 1 <= len(g) <= 200 and 1 <= len(g[0]) <= 200
        assert all(
            len(row) == len(g[0]) and all(-1000 <= x <= 1000 for x in row) for row in g
        )
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(dungeon=[[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
    add(dungeon=[[0]])
    add(dungeon=[[-1000] * 200 for _ in range(200)])
    add(dungeon=[[1000] * 200 for _ in range(200)])
    add(dungeon=[[-1000]])
    while len(calls) < 600:
        m, n = rng.randint(1, 10), rng.randint(1, 10)
        g = [[rng.randint(-30, 30) for _ in range(n)] for _ in range(m)]
        if len(calls) % 5 == 0:
            g = [[-abs(x) for x in row] for row in g]
        add(dungeon=g)
    return calls
