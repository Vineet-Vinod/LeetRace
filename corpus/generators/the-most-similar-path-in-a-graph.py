import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(
        n: int, roads: list[list[int]], names: list[str], targetPath: list[str]
    ) -> None:
        assert 2 <= n <= 100 and n - 1 <= len(roads) <= n * (n - 1) // 2
        assert len({tuple(sorted(e)) for e in roads}) == len(roads) and all(
            len(e) == 2 and 0 <= e[0] < n and 0 <= e[1] < n and e[0] != e[1]
            for e in roads
        )
        reached = {0}
        while True:
            old = len(reached)
            for a, b in roads:
                if a in reached or b in reached:
                    reached.update([a, b])
            if len(reached) == old:
                break
        assert len(reached) == n and len(names) == n and 1 <= len(targetPath) <= 100
        assert all(
            len(s) == 3 and all("A" <= c <= "Z" for c in s) for s in names + targetPath
        )
        call = (
            "candidate("
            + ", ".join(
                f"{key}={value!r}"
                for key, value in [
                    ("n", n),
                    ("roads", roads),
                    ("names", names),
                    ("targetPath", targetPath),
                ]
            )
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    add(
        n=5,
        roads=[[0, 2], [0, 3], [1, 2], [1, 3], [1, 4], [2, 4]],
        names=["ATL", "PEK", "LAX", "DXB", "HND"],
        targetPath=["ATL", "DXB", "HND", "LAX"],
    )
    add(
        n=100,
        roads=[[i, j] for i in range(100) for j in range(i + 1, 100)],
        names=["AAA"] * 100,
        targetPath=["BBB"] * 100,
    )
    add(
        n=100,
        roads=[[i - 1, i] for i in range(1, 100)],
        names=["AAA"] * 100,
        targetPath=["AAA"] * 100,
    )
    add(
        n=5,
        roads=[[0, 2], [0, 3], [1, 2], [1, 3], [1, 4], [2, 4]],
        names=["ATL", "PEK", "LAX", "DXB", "HND"],
        targetPath=["ATL", "DXB", "HND", "LAX"],
    )
    add(
        n=4,
        roads=[[1, 0], [2, 0], [3, 0], [2, 1], [3, 1], [3, 2]],
        names=["ATL", "PEK", "LAX", "DXB"],
        targetPath=["ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX"],
    )
    add(
        n=6,
        roads=[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],
        names=["ATL", "PEK", "LAX", "ATL", "DXB", "HND"],
        targetPath=["ATL", "DXB", "HND", "DXB", "ATL", "LAX", "PEK"],
    )
    while len(calls) < 600:
        n = rng.randint(2, 12)
        roads = {(rng.randrange(i), i) for i in range(1, n)}
        for _ in range(rng.randint(0, n * n)):
            a, b = sorted(rng.sample(range(n), 2))
            roads.add((a, b))
        names = [rng.choice(["AAA", "BBB", "CCC", "DDD"]) for _ in range(n)]
        length = rng.randint(1, 18)
        if len(calls) % 3 == 0:
            node = rng.randrange(n)
            target = [names[node]]
            for _ in range(length - 1):
                neighbors = [b if a == node else a for a, b in roads if node in (a, b)]
                node = rng.choice(sorted(neighbors))
                target.append(names[node])
        else:
            target = [rng.choice(["AAA", "BBB", "CCC", "EEE"]) for _ in range(length)]
        add(n=n, roads=[list(e) for e in sorted(roads)], names=names, targetPath=target)
    return calls
