import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty positive-integer arrays and k in [0,len(arr)]."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        arr = [rng.randrange(1, 10001) for _ in range(1 + i % 60)]
        k = (i * 7) % len(arr)
        call = f"candidate(arr={arr!r}, k={k})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
