import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty positive arrays and positive targets in the stated bounds."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        nums = [rng.randrange(1, 10**6 + 1) for _ in range(1 + i % 60)]
        target = rng.randrange(1, 10**6 + 1)
        call = f"candidate(nums={nums!r}, target={target})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
