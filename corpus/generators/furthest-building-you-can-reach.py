import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty height arrays and nonnegative resource counts."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        heights = [rng.randrange(1, 100001) for _ in range(1 + i % 50)]
        bricks = rng.randrange(0, 100001)
        ladders = i % (len(heights) + 1)
        call = f"candidate(heights={heights!r}, bricks={bricks}, ladders={ladders})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
