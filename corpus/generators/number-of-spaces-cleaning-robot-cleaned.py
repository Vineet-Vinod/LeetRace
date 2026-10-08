import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty binary rooms whose top-left cell is empty."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        m = 1 + i % 12
        n = 1 + (i * 7) % 12
        room = [[rng.randrange(2) for _ in range(n)] for _ in range(m)]
        room[0][0] = 0
        call = f"candidate(room={room!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
