import random


def generate(seed: int = 0) -> list[str]:
    """Represent nonnegative decimal integers without leading zeros (zero is [0])."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 1 + i % 35
        vals = [rng.randrange(1, 10)] + [rng.randrange(10) for _ in range(n - 1)]
        if i % 17 == 0:
            vals = [0]
        call = f"candidate(head=list_node({vals!r}))"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
