import random


def generate(seed: int = 0) -> list[str]:
    """Color and needed-time arrays have equal nonzero length and legal values."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 1 + i % 60
        colors = "".join(rng.choice("abcde") for _ in range(n))
        times = [rng.randrange(1, 10001) for _ in range(n)]
        call = f"candidate(colors={colors!r}, neededTime={times!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
