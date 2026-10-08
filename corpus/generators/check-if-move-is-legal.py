import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[str, ...], int, int, str]] = set()
    for _ in range(700):
        board = [[rng.choice("BW.") for _ in range(8)] for _ in range(8)]
        row, col = rng.randrange(8), rng.randrange(8)
        board[row][col] = "."
        color = rng.choice("BW")
        cases.add((tuple("".join(line) for line in board), row, col, color))
    assert all(
        len(board) == 8
        and all(len(row) == 8 and set(row) <= {"B", "W", "."} for row in board)
        and board[r][c] == "."
        and color in "BW"
        for board, r, c, color in cases
    )
    return [
        f"candidate(board={[list(row) for row in board]!r}, rMove={r}, cMove={c}, color={color!r})"
        for board, r, c, color in sorted(cases)
    ][:600]
