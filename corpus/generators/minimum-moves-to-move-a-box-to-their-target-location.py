import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        a = data["grid"]
        assert (
            1 <= len(a) <= 20
            and 1 <= len(a[0]) <= 20
            and all(len(row) == len(a[0]) for row in a)
        )
        flat = [c for row in a for c in row]
        assert set(flat) <= set(".#SBT") and all(flat.count(c) == 1 for c in "SBT")
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [
        {
            "grid": [
                ["#", "#", "#", "#", "#", "#"],
                ["#", "T", "#", "#", "#", "#"],
                ["#", ".", ".", "B", ".", "#"],
                ["#", ".", "#", "#", ".", "#"],
                ["#", ".", ".", ".", "S", "#"],
                ["#", "#", "#", "#", "#", "#"],
            ]
        },
        {
            "grid": [
                ["#", "#", "#", "#", "#", "#"],
                ["#", "T", "#", "#", "#", "#"],
                ["#", ".", ".", "B", ".", "#"],
                ["#", "#", "#", "#", ".", "#"],
                ["#", ".", ".", ".", "S", "#"],
                ["#", "#", "#", "#", "#", "#"],
            ]
        },
        {
            "grid": [
                ["#", "#", "#", "#", "#", "#"],
                ["#", "T", ".", ".", "#", "#"],
                ["#", ".", "#", "B", ".", "#"],
                ["#", ".", ".", ".", ".", "#"],
                ["#", ".", ".", ".", "S", "#"],
                ["#", "#", "#", "#", "#", "#"],
            ]
        },
    ]:
        add(**example)
    add(grid=[list("SBT")])
    add(grid=[list("BST")])
    large = [["."] * 20 for _ in range(20)]
    large[0][0] = "S"
    large[1][1] = "B"
    large[18][18] = "T"
    add(grid=large)
    while len(calls) < 600:
        rows, cols = rng.randint(3, 7), rng.randint(3, 7)
        board = [["."] * cols for _ in range(rows)]
        if len(calls) % 2 == 0:
            # An open rectangular board and interior box provide constructive solvable cases.
            bx, by = rng.randrange(1, rows - 1), rng.randrange(1, cols - 1)
            choices = [
                (x, y) for x in range(rows) for y in range(cols) if (x, y) != (bx, by)
            ]
            target, player = rng.sample(choices, 2)
            board[bx][by] = "B"
            board[target[0]][target[1]] = "T"
            board[player[0]][player[1]] = "S"
        else:
            for x in range(rows):
                for y in range(cols):
                    if rng.random() < 0.35:
                        board[x][y] = "#"
            for marker, cell in zip(
                "SBT", rng.sample([(x, y) for x in range(rows) for y in range(cols)], 3)
            ):
                board[cell[0]][cell[1]] = marker
        add(grid=board)
    assert len(calls) == 600
    return calls
