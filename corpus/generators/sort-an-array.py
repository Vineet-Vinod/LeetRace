import random


def generate(seed: int = 0) -> list[str]:
    """Generate integer arrays within [-50000,50000], including duplicates."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        nums = [rng.randrange(-50000, 50001) for _ in range(1 + i % 100)]
        call = f"candidate(nums={nums!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
