import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(status, candies, keys, containedBoxes, initialBoxes):
        n = len(status)
        assert 1 <= n <= 1000 and len(candies) == len(keys) == len(containedBoxes) == n
        assert all(s in (0, 1) for s in status) and all(1 <= c <= 1000 for c in candies)
        assert all(
            len(k) <= n and len(set(k)) == len(k) and all(0 <= v < n for v in k)
            for k in keys
        )
        assert all(
            len(c) <= n and len(set(c)) == len(c) and all(0 <= v < n for v in c)
            for c in containedBoxes
        )
        children = [v for c in containedBoxes for v in c]
        assert len(children) == len(set(children))
        assert len(initialBoxes) <= n and all(0 <= v < n for v in initialBoxes)
        call = (
            "candidate("
            + ", ".join(
                f"{name}={value!r}"
                for name, value in (
                    ("status", status),
                    ("candies", candies),
                    ("keys", keys),
                    ("containedBoxes", containedBoxes),
                    ("initialBoxes", initialBoxes),
                )
            )
            + ")"
        )
        calls[call] = None

    add(
        status=[1, 0, 1, 0],
        candies=[7, 5, 4, 100],
        keys=[[], [], [1], []],
        containedBoxes=[[1, 2], [3], [], []],
        initialBoxes=[0],
    )
    add(
        status=[1, 0, 0, 0, 0, 0],
        candies=[1, 1, 1, 1, 1, 1],
        keys=[[1, 2, 3, 4, 5], [], [], [], [], []],
        containedBoxes=[[1, 2, 3, 4, 5], [], [], [], [], []],
        initialBoxes=[0],
    )
    add(
        status=[1] + [0] * 999,
        candies=[1000] * 1000,
        keys=[list(range(1000))] + [[] for _ in range(999)],
        containedBoxes=[list(range(1, 1000))] + [[] for _ in range(999)],
        initialBoxes=[0],
    )
    add(
        status=[1] * 1000,
        candies=[1] * 1000,
        keys=[[] for _ in range(1000)],
        containedBoxes=[[] for _ in range(1000)],
        initialBoxes=list(range(1000)),
    )
    while len(calls) < 600:
        n = rng.randint(1, 25)
        status = [rng.randint(0, 1) for _ in range(n)]
        candies = [rng.randint(1, 1000) for _ in range(n)]
        keys = [rng.sample(range(n), rng.randint(0, min(n, 5))) for _ in range(n)]
        contained = [[] for _ in range(n)]
        for child in range(1, n):
            if rng.random() < 0.7:
                contained[rng.randrange(child)].append(child)
        mode = rng.randrange(4)
        if mode == 0:
            status = [1] * n
            initial = list(range(n))
        elif mode == 1:
            status = [0] * n
            initial = rng.sample(range(n), rng.randint(0, n))
        elif mode == 2:
            status[0] = 1
            contained = [[i + 1] if i + 1 < n else [] for i in range(n)]
            keys = [[i + 1] if i + 1 < n else [] for i in range(n)]
            initial = [0]
        else:
            initial = rng.sample(range(n), rng.randint(0, n))
        add(
            status=status,
            candies=candies,
            keys=keys,
            containedBoxes=contained,
            initialBoxes=initial,
        )
    return list(calls)
