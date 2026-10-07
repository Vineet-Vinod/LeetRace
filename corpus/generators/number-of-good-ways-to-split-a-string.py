import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty lowercase strings."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        s = "".join(rng.choice("abcdef") for _ in range(1 + i % 70))
        call = f"candidate(s={s!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
