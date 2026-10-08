import random


def generate(seed: int = 0) -> list[str]:
    """Generate nonempty lowercase strings within the stated length bounds."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        word1 = "".join(
            rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(1 + i % 40)
        )
        word2 = "".join(
            rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(1 + (i * 7) % 40)
        )
        call = f"candidate(word1={word1!r}, word2={word2!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
