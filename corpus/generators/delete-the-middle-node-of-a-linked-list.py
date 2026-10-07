import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty linked-list values within the problem bounds."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        vals = [rng.randrange(0, 100001) for _ in range(1 + i % 40)]
        call = f"candidate(head=list_node({vals!r}))"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
