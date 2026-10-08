import random


def generate(seed: int = 0) -> list[str]:
    r = random.Random(seed)
    cases = []
    seen = set()

    def add(groups):
        n = len(groups)
        grid = [
            [int(i == j or groups[i] == groups[j]) for j in range(n)] for i in range(n)
        ]
        key = tuple(map(tuple, grid))
        if key not in seen:
            assert 1 <= n <= 200 and all(
                grid[i][j] == grid[j][i] for i in range(n) for j in range(n)
            )
            seen.add(key)
            cases.append(f"candidate(isConnected={grid!r})")

    for n in range(1, 40):
        for components in range(1, n + 1):
            add([i % components for i in range(n)])
    for _ in range(300):
        n = r.randint(2, 200)
        c = r.randint(1, n)
        add([r.randrange(c) for _ in range(n)])
    add([i for i in range(200)])
    add([0] * 200)
    return cases[:800] + [cases[-1]] if len(cases) > 800 else cases
