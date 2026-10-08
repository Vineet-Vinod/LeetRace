import random


def generate(seed: int = 0) -> list[str]:
    """Generate lowercase nonempty strings within the 300000-character limit."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        s = "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(1 + i % 70))
        call = f"candidate(s={s!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
