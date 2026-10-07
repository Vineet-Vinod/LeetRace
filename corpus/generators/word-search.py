import random
import string


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases: set[tuple[tuple[tuple[str, ...], ...], str]] = set()
    # Fixed canonical examples and both one-cell outcomes.
    cases.add(((("A",),), "A"))
    cases.add(((("A",),), "B"))
    cases.add((tuple(tuple("A" for _ in range(6)) for _ in range(6)), "A" * 15))
    while len(cases) < 600:
        rows, cols = rng.randint(1, 6), rng.randint(1, 6)
        alphabet = "ABC" if rng.random() < 0.65 else string.ascii_letters
        board = tuple(
            tuple(rng.choice(alphabet) for _ in range(cols)) for _ in range(rows)
        )
        if rng.random() < 0.5:
            row, col = rng.randrange(rows), rng.randrange(cols)
            length = rng.randint(1, min(15, rows * cols))
            word = [board[row][col]]
            visited = {(row, col)}
            for _ in range(length - 1):
                neighbors = [
                    (r, c)
                    for r, c in (
                        (row - 1, col),
                        (row + 1, col),
                        (row, col - 1),
                        (row, col + 1),
                    )
                    if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited
                ]
                if not neighbors:
                    break
                row, col = rng.choice(neighbors)
                visited.add((row, col))
                word.append(board[row][col])
            word_text = "".join(word)
        else:
            word_text = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, 15)))
        cases.add((board, word_text))
    assert all(
        1 <= len(board) <= 6
        and 1 <= len(board[0]) <= 6
        and all(
            len(row) == len(board[0])
            and all(char in string.ascii_letters for char in row)
            for row in board
        )
        and 1 <= len(word) <= 15
        and all(char in string.ascii_letters for char in word)
        for board, word in cases
    )
    return [
        f"candidate(board={[list(row) for row in board]!r}, word={word!r})"
        for board, word in sorted(cases)
    ]
