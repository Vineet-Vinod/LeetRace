import random


def generate(seed: int = 0) -> list[str]:
    """Generate lowercase nonempty words with lengths within the task bound."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        word = "".join(
            rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(1 + i % 100)
        )
        call = f"candidate(word={word!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
