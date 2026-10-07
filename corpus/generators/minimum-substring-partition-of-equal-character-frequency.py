import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty lowercase strings within the 1000-character bound."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        s = "".join(rng.choice("abcde") for _ in range(1 + i % 60))
        call = f"candidate(s={s!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
