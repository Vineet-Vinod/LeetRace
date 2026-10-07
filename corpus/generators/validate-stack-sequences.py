import random


def generate(seed: int = 0) -> list[str]:
    """Generate distinct pushed values and popped as a permutation of pushed."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        pushed = rng.sample(range(0, 1001), 1 + i % 60)
        popped = pushed.copy()
        rng.shuffle(popped)
        call = f"candidate(pushed={pushed!r}, popped={popped!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
