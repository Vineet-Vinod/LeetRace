import random


def generate(seed: int = 0) -> list[str]:
    """Generate digit strings of legal length 4..12, including valid and invalid addresses."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        n = 4 + i % 9
        s = "".join(rng.choice("0123456789") for _ in range(n))
        call = f"candidate(s={s!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
