import random


def generate(seed: int = 0) -> list[str]:
    """Generate arrays of positive integers within the problem's digit/value bounds."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        nums = [rng.randint(1, 10**6) for _ in range(1 + i % 30)]
        assert nums and all(1 <= x <= 10**6 for x in nums)
        call = f"candidate(nums={nums!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
