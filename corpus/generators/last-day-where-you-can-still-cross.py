import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: dict[str, None] = {}

    def add(row, col, cells):
        assert 2 <= row <= 20000 and 2 <= col <= 20000 and 4 <= row * col <= 20000
        assert len(cells) == row * col
        assert {tuple(c) for c in cells} == {
            (r, c) for r in range(1, row + 1) for c in range(1, col + 1)
        }
        call = (
            "candidate("
            + ", ".join(
                f"{name}={value!r}"
                for name, value in (
                    ("row", row),
                    ("col", col),
                    ("cells", cells),
                )
            )
            + ")"
        )
        calls[call] = None

    add(row=2, col=2, cells=[[1, 1], [2, 1], [1, 2], [2, 2]])
    add(row=2, col=2, cells=[[1, 1], [1, 2], [2, 1], [2, 2]])
    add(
        row=3,
        col=3,
        cells=[[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]],
    )
    add(row=2, col=10000, cells=[[r, c] for r in (1, 2) for c in range(1, 10001)])
    add(row=10000, col=2, cells=[[r, c] for r in range(1, 10001) for c in (1, 2)])
    while len(calls) < 600:
        row, col = rng.randint(2, 9), rng.randint(2, 9)
        cells = [[r, c] for r in range(1, row + 1) for c in range(1, col + 1)]
        mode = rng.randrange(3)
        if mode == 0:
            rng.shuffle(cells)
        elif mode == 1:
            cells.sort(key=lambda c: (c[1], c[0]))
        else:
            cells.sort(key=lambda c: (c[0], -c[1]))
            # A legal permutation with a changed flood order, not duplicate padding.
            a, b = rng.sample(range(len(cells)), 2)
            cells[a], cells[b] = cells[b], cells[a]
        add(row=row, col=col, cells=cells)
    return list(calls)
