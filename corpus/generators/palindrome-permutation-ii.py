import random


def generate(seed: int = 0) -> list[str]:
    """Generate lowercase strings with legal length 1..16, often with repeated letters."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        s = "".join(rng.choice("abcde") for _ in range(1 + i % 16))
        call = f"candidate(s={s!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
