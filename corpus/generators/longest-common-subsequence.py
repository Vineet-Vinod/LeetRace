import random


def generate(seed: int = 0) -> list[str]:
    """Generate lowercase strings with legal nonzero lengths and moderate sizes."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        a = "".join(rng.choice("abcd") for _ in range(1 + i % 35))
        b = "".join(rng.choice("abcd") for _ in range(1 + (i * 7) % 35))
        call = f"candidate(text1={a!r}, text2={b!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
