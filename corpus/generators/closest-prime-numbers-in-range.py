import random


def generate(seed: int = 0) -> list[str]:
    """Generate valid 1 <= left <= right <= 1,000,000 ranges, mostly narrow for fast tests."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        left = 1 + rng.randrange(9900)
        right = min(10**6, left + rng.randrange(1, 100))
        call = f"candidate(left={left}, right={right})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
