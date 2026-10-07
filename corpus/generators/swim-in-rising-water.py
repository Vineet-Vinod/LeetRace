import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**kwargs):
        g = kwargs["grid"]
        n = len(g)
        assert 1 <= n <= 50 and all(len(row) == n for row in g)
        assert sorted(x for row in g for x in row) == list(range(n * n))
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in kwargs.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(grid=[[0, 2], [1, 3]])
    add(
        grid=[
            [0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6],
        ]
    )
    add(grid=[[50 * i + j for j in range(50)] for i in range(50)])
    add(grid=[[0]])
    while len(calls) < 600:
        n = rng.randint(2, 12)
        a = list(range(n * n))
        rng.shuffle(a)
        add(grid=[a[i * n : (i + 1) * n] for i in range(n)])
    return calls
