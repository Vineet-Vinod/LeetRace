import random

_STATEMENT_EXAMPLES = (
    "candidate(board=[['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', 'p', '.', '.', '.', '.'], ['.', '.', '.', 'R', '.', '.', '.', 'p'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', 'p', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.']])",
    "candidate(board=[['.', '.', '.', '.', '.', '.', '.', '.'], ['.', 'p', 'p', 'p', 'p', 'p', '.', '.'], ['.', 'p', 'p', 'B', 'p', 'p', '.', '.'], ['.', 'p', 'B', 'R', 'B', 'p', '.', '.'], ['.', 'p', 'p', 'B', 'p', 'p', '.', '.'], ['.', 'p', 'p', 'p', 'p', 'p', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.']])",
    "candidate(board=[['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', 'p', '.', '.', '.', '.'], ['.', '.', '.', 'p', '.', '.', '.', '.'], ['p', 'p', '.', 'R', '.', 'p', 'B', '.'], ['.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', 'B', '.', '.', '.', '.'], ['.', '.', '.', 'p', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.']])",
)


def generate(seed: int = 0) -> list[str]:
    """Generate 600 distinct 8x8 boards with one rook and at most eight pawns."""
    rng = random.Random(seed)
    calls: list[str] = []
    seen: set[str] = set()
    while len(calls) < 600:
        board = [["." for _ in range(8)] for _ in range(8)]
        rr, rc = rng.randrange(8), rng.randrange(8)
        board[rr][rc] = "R"
        occupied = {(rr, rc)}
        for _ in range(rng.randrange(9)):
            r, c = rng.randrange(8), rng.randrange(8)
            if (r, c) not in occupied:
                board[r][c] = rng.choice(("p", "B"))
                occupied.add((r, c))
        call = f"candidate(board={board!r})"
        if call not in seen:
            calls.append(call)
            seen.add(call)
    return calls


_BASE_GENERATE = generate


def generate(seed: int = 0) -> list[str]:
    calls = list(_STATEMENT_EXAMPLES)
    seen = set(calls)
    for call in _BASE_GENERATE(seed):
        if call not in seen:
            calls.append(call)
            seen.add(call)
    limit = globals().get("DOMAIN_SIZE", 600)
    if len(calls) < limit:
        raise ValueError("Generator did not produce enough distinct cases")
    return calls[:limit]
