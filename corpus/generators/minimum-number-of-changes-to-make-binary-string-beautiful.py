import random


def generate(seed: int = 0) -> list[str]:
    """Generate even-length binary strings within the stated length limit."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 2 + 2 * (i % 50)
        s = "".join(rng.choice("01") for _ in range(n))
        call = f"candidate(s={s!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
