import random


def generate(seed: int = 0) -> list[str]:
    """Generate positive positions and step counts in 1..1000."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        start = rng.randrange(1, 1001)
        end = rng.randrange(1, 1001)
        k = rng.randrange(1, 1001)
        call = f"candidate(startPos={start}, endPos={end}, k={k})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
