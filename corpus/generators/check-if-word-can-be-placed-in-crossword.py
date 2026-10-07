import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    cases = {
        ((("#", " ", "#"), (" ", " ", "#"), ("#", "c", " ")), "abc"),
        (((" ", "#", "a"), (" ", "#", "c"), (" ", "#", "a")), "ac"),
    }
    while len(cases) < 600:
        rows, cols = rng.randint(1, 12), rng.randint(1, 12)
        board = tuple(
            tuple(rng.choice((" ", "#", "a", "b", "c")) for _ in range(cols))
            for _ in range(rows)
        )
        word = "".join(
            rng.choice("abc") for _ in range(rng.randint(1, max(rows, cols)))
        )
        cases.add((board, word))
    return [
        f"candidate(board={[list(row) for row in board]!r}, word={word!r})"
        for board, word in cases
    ]
