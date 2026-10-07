import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty arrays and valid inclusive request intervals."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 1 + i % 50
        nums = [rng.randrange(0, 100001) for _ in range(n)]
        requests = []
        for _ in range(1 + i % 20):
            left = rng.randrange(n)
            right = rng.randrange(left, n)
            requests.append([left, right])
        call = f"candidate(nums={nums!r}, requests={requests!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
