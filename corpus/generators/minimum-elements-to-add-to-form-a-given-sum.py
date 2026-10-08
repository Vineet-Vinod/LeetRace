import random


def generate(seed: int = 0) -> list[str]:
    """Generate bounded signed array entries, positive limit, and signed goal."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        limit = 1 + (i * 7) % 1000
        nums = [rng.randrange(-limit, limit + 1) for _ in range(1 + i % 50)]
        goal = rng.randrange(-100000, 100001)
        call = f"candidate(nums={nums!r}, limit={limit}, goal={goal})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
