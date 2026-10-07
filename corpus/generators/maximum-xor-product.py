import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonnegative a,b and n in the legal bit range."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = i % 51
        a = rng.randrange(0, 250)
        b = rng.randrange(0, 250)
        call = f"candidate(a={a}, b={b}, n={n})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
