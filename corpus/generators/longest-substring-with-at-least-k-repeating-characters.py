import random


def generate(seed: int = 0) -> list[str]:
    """Generate lowercase nonempty strings and positive k values."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        s = "".join(rng.choice("abcde") for _ in range(1 + i % 60))
        k = 1 + (i * 7) % 70
        call = f"candidate(s={s!r}, k={k})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
