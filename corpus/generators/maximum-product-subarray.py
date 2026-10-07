import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty arrays with values in [-10,10], including zeros and negatives."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        nums = [rng.randrange(-10, 11) for _ in range(1 + i % 50)]
        call = f"candidate(nums={nums!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
