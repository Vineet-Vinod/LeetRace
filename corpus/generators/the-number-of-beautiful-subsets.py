import random


def generate(seed: int = 0) -> list[str]:
    """Generate arrays of 1..18 positive values and positive k."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 18 if i == 0 else 1 + i % 12
        nums = [rng.randrange(1, 1001) for _ in range(n)]
        k = 1 + (i * 7) % 1000
        call = f"candidate(nums={nums!r}, k={k})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
