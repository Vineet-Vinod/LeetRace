import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty integer arrays; values remain in the stated positive range."""
    rng = random.Random(seed)
    calls = [
        "candidate(nums=[10, 6, 5, 8])",
        "candidate(nums=[1, 3, 5, 3])",
    ]
    seen = set(calls)
    i = 0
    while len(calls) < 600:
        nums = [rng.randrange(1, 100001) for _ in range(1 + i % 40)]
        call = f"candidate(nums={nums!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
