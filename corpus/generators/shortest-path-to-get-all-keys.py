import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()

    def add(**data) -> None:
        a = data["grid"]
        assert (
            1 <= len(a) <= 30
            and 1 <= len(a[0]) <= 30
            and all(len(row) == len(a[0]) for row in a)
        )
        s = "".join(a)
        assert s.count("@") == 1 and set(s) <= set(".#@abcdefABCDEF")
        k = sum(s.count(c) for c in "abcdef")
        assert 1 <= k <= 6
        for i in range(6):
            assert s.count(chr(97 + i)) == s.count(chr(65 + i)) == (1 if i < k else 0)
        call = (
            "candidate("
            + ", ".join(f"{key}={value!r}" for key, value in data.items())
            + ")"
        )
        if call not in seen:
            seen.add(call)
            calls.append(call)

    for example in [
        {"grid": ["@.a..", "###.#", "b.A.B"]},
        {"grid": ["@..aA", "..B#.", "....b"]},
        {"grid": ["@Aa"]},
    ]:
        add(**example)
    add(grid=["@aA"])
    add(grid=["@Aa"])
    board = [list("." * 30) for _ in range(30)]
    board[0][0] = "@"
    for i, c in enumerate("abcdefABCDEF"):
        board[29][i] = c
    add(grid=["".join(row) for row in board])
    while len(calls) < 600:
        rows, cols = rng.randint(3, 8), rng.randint(5, 10)
        k = rng.randint(1, min(6, (rows * cols - 1) // 2))
        board = [["."] * cols for _ in range(rows)]
        if len(calls) % 3 == 0:
            # All keys lie in a corridor reachable before any lock.
            flat = list(
                "@" + "abcdef"[:k] + "ABCDEF"[:k] + "." * (rows * cols - 1 - 2 * k)
            )
            board = [flat[i * cols : (i + 1) * cols] for i in range(rows)]
        else:
            for x in range(rows):
                for y in range(cols):
                    if rng.random() < 0.25:
                        board[x][y] = "#"
            cells = rng.sample(
                [(x, y) for x in range(rows) for y in range(cols)], 1 + 2 * k
            )
            for marker, cell in zip("@" + "abcdef"[:k] + "ABCDEF"[:k], cells):
                board[cell[0]][cell[1]] = marker
        add(grid=["".join(row) for row in board])
    assert len(calls) == 600
    return calls
