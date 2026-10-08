def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(board=[['5','3','.','.','7','.','.','.','.'],['6','.','.','1','9','5','.','.','.'],['.','9','8','.','.','.','.','6','.'],['8','.','.','.','6','.','.','.','3'],['4','.','.','8','.','3','.','.','1'],['7','.','.','.','2','.','.','.','6'],['.','6','.','.','.','.','2','8','.'],['.','.','.','4','1','9','.','.','5'],['.','.','.','.','8','.','.','7','9']])",
        "candidate(board=[['8','3','.','.','7','.','.','.','.'],['6','.','.','1','9','5','.','.','.'],['.','9','8','.','.','.','.','6','.'],['8','.','.','.','6','.','.','.','3'],['4','.','.','8','.','3','.','.','1'],['7','.','.','.','2','.','.','.','6'],['.','6','.','.','.','.','2','8','.'],['.','.','.','4','1','9','.','.','5'],['.','.','.','.','8','.','.','7','9']])",
    }

    def valid_board() -> list[list[str]]:
        digits = list("123456789")
        rng.shuffle(digits)
        bands = list(range(3))
        stacks = list(range(3))
        rng.shuffle(bands)
        rng.shuffle(stacks)
        rows = [
            band * 3 + offset for band in bands for offset in rng.sample(range(3), 3)
        ]
        cols = [
            stack * 3 + offset for stack in stacks for offset in rng.sample(range(3), 3)
        ]
        board = [[digits[(r * 3 + r // 3 + c) % 9] for c in cols] for r in rows]
        return board

    while len(cases) < 600:
        board = valid_board()
        if rng.random() < 0.6:
            for r in range(9):
                for c in range(9):
                    if rng.random() < 0.45:
                        board[r][c] = "."
        else:
            row = rng.randrange(9)
            c1, c2 = rng.sample(range(9), 2)
            board[row][c1] = board[row][c2]
        assert len(board) == 9 and all(len(row) == 9 for row in board)
        assert all(value in "123456789." for row in board for value in row)
        cases.add(f"candidate(board={board!r})")
    return sorted(cases)
