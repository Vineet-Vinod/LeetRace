import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    squares = [(r, c) for r in range(8) for c in range(8)]
    while len(calls) < 600:
        king = list(rng.choice(squares))
        options = [list(square) for square in squares if square != tuple(king)]
        queens = [rng.choice(options) for _ in range(rng.randint(1, 63))]
        queens = [list(x) for x in {tuple(q) for q in queens}]
        if not queens:
            queens = [[(king[0] + 1) % 8, king[1]]]
        calls.add(f"candidate(queens={queens!r}, king={king!r})")
    return sorted(calls)


_BASE_GENERATE = generate
_STATEMENT_EXAMPLE_CALLS = (
    "candidate(queens=[[0, 0], [1, 1], [2, 2], [3, 4], [3, 5], [4, 4], [4, 5]], king=[3, 3])",
    "candidate(queens=[[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]], king=[0, 0])",
)


def generate(seed: int = 0) -> list[str]:
    return sorted(set(_BASE_GENERATE(seed)) | set(_STATEMENT_EXAMPLE_CALLS))
