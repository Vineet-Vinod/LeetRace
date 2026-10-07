import random


def generate(seed: int = 0) -> list[str]:
    """Generate sorted lists of 0..100 values, including repeated runs."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        vals = sorted(rng.randrange(-100, 101) for _ in range(i % 50))
        call = f"candidate(head=list_node({vals!r}))"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
