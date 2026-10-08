import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    while len(calls) < 600:
        cells = [(row, column) for row in range(3) for column in range(3)]
        rng.shuffle(cells)
        moves: list[list[int]] = []
        board = [["" for _ in range(3)] for _ in range(3)]
        for index, (row, column) in enumerate(cells):
            moves.append([row, column])
            board[row][column] = "A" if index % 2 == 0 else "B"
            lines = board + [[board[r][c] for r in range(3)] for c in range(3)]
            lines += [
                [board[i][i] for i in range(3)],
                [board[i][2 - i] for i in range(3)],
            ]
            if any(line[0] and line.count(line[0]) == 3 for line in lines):
                break
        assert len(moves) <= 9 and len({tuple(move) for move in moves}) == len(moves)
        calls.add(f"candidate(moves={moves!r})")
    return sorted(calls)
