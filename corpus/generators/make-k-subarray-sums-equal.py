import random


def generate(seed: int = 0) -> list[str]:
    """Generate positive integer arrays and 1 <= k <= n."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 1 + i % 50
        arr = [rng.randrange(1, 10**5 + 1) for _ in range(n)]
        k = 1 + (i * 7) % n
        call = f"candidate(arr={arr!r}, k={k})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
