import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty arrays of positive integers within the 10^9 bound."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        nums = [rng.randrange(1, 10**9 + 1) for _ in range(1 + i % 60)]
        call = f"candidate(nums={nums!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
