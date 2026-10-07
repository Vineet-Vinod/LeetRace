import random


def generate(seed: int = 0) -> list[str]:
    """Generate positive bag sizes and a nonnegative operation budget."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        nums = [rng.randrange(1, 100001) for _ in range(1 + i % 50)]
        ops = rng.randrange(1, 100001)
        call = f"candidate(nums={nums!r}, maxOperations={ops})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
