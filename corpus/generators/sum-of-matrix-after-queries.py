import random


def generate(seed: int = 0) -> list[str]:
    """Generate row/column assignments with valid indexes, types, and values."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 1 + i % 30
        queries = [
            [rng.randrange(2), rng.randrange(n), rng.randrange(100001)]
            for _ in range(1 + i % 40)
        ]
        call = f"candidate(n={n}, queries={queries!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
