import random


def generate(seed: int = 0) -> list[str]:
    """Generate unique lowercase words, all with equal length."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        width = 1 + i % 12
        words = set()
        while len(words) < 1 + (i % 20):
            words.add(
                "".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(width))
            )
        values = sorted(words)
        call = f"candidate(dict={values!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
