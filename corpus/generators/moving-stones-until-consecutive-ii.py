import random


def generate(seed: int = 0) -> list[str]:
    """Generate 3..50 unique positive stone coordinates in arbitrary input order."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 3 + i % 48
        stones = rng.sample(range(1, 100001), n)
        call = f"candidate(stones={stones!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
