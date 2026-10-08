import random


def generate(seed: int = 0) -> list[str]:
    """Generate integer arrays and 1 <= k <= n within stated value bounds."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 1 + i % 50
        nums = [rng.randrange(1, 101) for _ in range(n)]
        k = 1 + (i * 7) % n
        call = f"candidate(nums={nums!r}, k={k})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
