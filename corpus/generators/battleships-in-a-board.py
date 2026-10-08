def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases: set[str] = set()

    def add(board: list[list[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        assert 1 <= rows <= 200 and 1 <= cols <= 200
        assert all(len(row) == cols for row in board)
        assert all(cell in {".", "X"} for row in board for cell in row)
        cases.add(f"candidate(board={board!r})")

    # Empty boards exercise zero ships at both small and maximum dimensions.
    for rows, cols in [(1, 1), (1, 200), (200, 1), (200, 200), (2, 7), (7, 2)]:
        add([["." for _ in range(cols)] for _ in range(rows)])

    # Single ships include both orientations, varied lengths, and all boundaries.
    for length in range(1, 31):
        board = [["." for _ in range(32)] for _ in range(32)]
        for col in range(length):
            board[0][col] = "X"
        add(board)
        board = [["." for _ in range(32)] for _ in range(32)]
        for row in range(length):
            board[row][-1] = "X"
        add(board)
    for row, col in [(0, 0), (0, 199), (199, 0), (199, 199)]:
        board = [["." for _ in range(200)] for _ in range(200)]
        board[row][col] = "X"
        add(board)

    # Maximum-boundary boards also contain several legal ships.
    board = [["." for _ in range(200)] for _ in range(200)]
    for row in range(0, 200, 2):
        board[row][0] = "X"
        board[row][1] = "X"
    add(board)
    board = [["." for _ in range(200)] for _ in range(200)]
    for col in range(0, 200, 2):
        board[0][col] = "X"
        board[1][col] = "X"
    add(board)

    # Place straight ships only when their eight-neighborhood is free, making
    # every fleet legal and preventing any bent or overlapping ship shapes.
    while len(cases) < 600:
        rows = rng.randint(1, 12)
        cols = rng.randint(1, 12)
        board = [["." for _ in range(cols)] for _ in range(rows)]
        occupied: set[tuple[int, int]] = set()
        ships = rng.randint(0, 8)
        attempts = 0
        while ships and attempts < 100:
            attempts += 1
            horizontal = bool(rng.randrange(2))
            limit = cols if horizontal else rows
            length = rng.randint(1, min(6, limit))
            row = rng.randrange(rows if horizontal else rows - length + 1)
            col = rng.randrange(cols - length + 1 if horizontal else cols)
            cells = [
                (row, col + offset) if horizontal else (row + offset, col)
                for offset in range(length)
            ]
            neighbors = {
                (r + dr, c + dc)
                for r, c in cells
                for dr in (-1, 0, 1)
                for dc in (-1, 0, 1)
            }
            if neighbors & occupied:
                continue
            for r, c in cells:
                board[r][c] = "X"
                occupied.add((r, c))
            ships -= 1
        add(board)

    result = list(cases)
    rng.shuffle(result)
    return result
