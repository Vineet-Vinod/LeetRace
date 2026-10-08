import random


def generate(seed: int = 0) -> list[str]:
    """Every query value lies in 1..m and the query list has length at most m."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        m = 1 + i % 60
        queries = [rng.randrange(1, m + 1) for _ in range(1 + (i * 7) % m)]
        call = f"candidate(queries={queries!r}, m={m})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
