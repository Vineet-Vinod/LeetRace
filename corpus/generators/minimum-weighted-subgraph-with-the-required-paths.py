import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(n, edges, src1, src2, dest):
        assert 3 <= n <= 100000 and 0 <= len(edges) <= 100000
        assert all(
            len(e) == 3
            and 0 <= e[0] < n
            and 0 <= e[1] < n
            and e[0] != e[1]
            and 1 <= e[2] <= 100000
            for e in edges
        )
        assert len({src1, src2, dest}) == 3 and all(
            0 <= v < n for v in (src1, src2, dest)
        )
        call = (
            "candidate("
            + ", ".join(
                f"{name}={value!r}"
                for name, value in (
                    ("n", n),
                    ("edges", edges),
                    ("src1", src1),
                    ("src2", src2),
                    ("dest", dest),
                )
            )
            + ")"
        )
        calls[call] = None

    add(
        n=6,
        edges=[
            [0, 2, 2],
            [0, 5, 6],
            [1, 0, 3],
            [1, 4, 5],
            [2, 1, 1],
            [2, 3, 3],
            [2, 3, 4],
            [3, 4, 2],
            [4, 5, 1],
        ],
        src1=0,
        src2=1,
        dest=5,
    )
    add(n=3, edges=[[0, 1, 1], [2, 1, 1]], src1=0, src2=1, dest=2)
    add(
        n=100000,
        edges=[[i, i + 1, 100000] for i in range(99999)] + [[0, 99999, 100000]],
        src1=0,
        src2=1,
        dest=99999,
    )
    add(n=100000, edges=[], src1=0, src2=1, dest=99999)
    while len(calls) < 600:
        n = rng.randint(3, 20)
        src1, src2, dest = rng.sample(range(n), 3)
        mode = rng.randrange(4)
        if mode == 0:
            edges = [[src1, dest, rng.randint(1, 30)], [src2, dest, rng.randint(1, 30)]]
        elif mode == 1:
            edges = []
        elif mode == 2:
            others = [i for i in range(n) if i not in (src1, src2, dest)]
            if others:
                middle = rng.choice(others)
                edges = [
                    [src1, middle, 1],
                    [src2, middle, 2],
                    [middle, dest, rng.randint(1, 30)],
                ]
            else:
                edges = [[src1, src2, 1], [src2, dest, 2]]
        else:
            edges = [
                rng.sample(range(n), 2) + [rng.randint(1, 100000)]
                for _ in range(rng.randint(1, 3 * n))
            ]
        add(n=n, edges=edges, src1=src1, src2=src2, dest=dest)
    return list(calls)
