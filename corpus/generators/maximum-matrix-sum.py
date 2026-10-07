import random


def generate(seed: int = 0) -> list[str]:
    """Generate square matrices with entries in [-100000,100000]."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 2 + i % 10
        matrix = [[rng.randrange(-100000, 100001) for _ in range(n)] for _ in range(n)]
        call = f"candidate(matrix={matrix!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
