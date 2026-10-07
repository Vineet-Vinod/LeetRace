import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty digit boards and rectangular letter/digit patterns within 50x50."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        m = 1 + i % 7
        n = 1 + (i * 7) % 7
        h = 1 + (i * 3) % m
        w = 1 + (i * 5) % n
        board = [[rng.randrange(10) for _ in range(n)] for _ in range(m)]
        pattern = [[rng.choice("0123456789abc") for _ in range(w)] for _ in range(h)]
        call = f"candidate(board={board!r}, pattern={pattern!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
