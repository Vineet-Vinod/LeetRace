import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty positive arrays and 1 <= k <= 15."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        nums = [rng.randrange(1, 10**9 + 1) for _ in range(1 + i % 40)]
        k = 1 + i % 15
        call = f"candidate(nums={nums!r}, k={k})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
