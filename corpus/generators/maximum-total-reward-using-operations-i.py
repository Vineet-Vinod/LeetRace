import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty arrays of distinct positive rewards."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 1 + i % 25
        values = sorted(rng.sample(range(1, 1001), n))
        call = f"candidate(rewardValues={values!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
