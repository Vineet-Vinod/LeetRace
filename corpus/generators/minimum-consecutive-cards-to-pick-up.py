import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty card arrays with positive labels."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        cards = [rng.randrange(1, 101) for _ in range(1 + i % 70)]
        call = f"candidate(cards={cards!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
