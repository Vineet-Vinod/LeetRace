import random


def generate(seed: int = 0) -> list[str]:
    """Generate sorted arrays where exactly one value occurs once and every other value twice."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        count = i % 25
        values = rng.sample(range(0, 100001), count + 1)
        single = values[0]
        nums = sorted([single] + [value for value in values[1:] for _ in range(2)])
        call = f"candidate(nums={nums!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
