def generate(seed: int = 0) -> list[str]:
    import random

    rng = random.Random(seed)
    cases = {
        "candidate(board=['O  ','   ','   '])",
        "candidate(board=['XOX',' X ','   '])",
        "candidate(board=['XOX', 'O O', 'XOX'])",
    }
    while len(cases) < 600:
        chars = [rng.choice("XO ") for _ in range(9)]
        board = ["".join(chars[i : i + 3]) for i in range(0, 9, 3)]
        assert len(board) == 3 and all(
            len(row) == 3 and set(row) <= {"X", "O", " "} for row in board
        )
        cases.add(f"candidate(board={board!r})")
    return sorted(cases)
