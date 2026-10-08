import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty integer arrays and p in [0,n//2]."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 1 + i % 50
        nums = [rng.randrange(0, 10**9 + 1) for _ in range(n)]
        p = (i * 7) % (n // 2 + 1)
        call = f"candidate(nums={nums!r}, p={p})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
