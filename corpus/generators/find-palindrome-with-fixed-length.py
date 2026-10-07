import random


def generate(seed: int = 0) -> list[str]:
    """Queries are positive ranks; lengths are legal and out-of-range ranks are included."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        length = 1 + i % 9
        qcount = 1 + i % 12
        queries = [rng.randrange(1, 10**9 + 1) for _ in range(qcount)]
        call = f"candidate(queries={queries!r}, intLength={length})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
