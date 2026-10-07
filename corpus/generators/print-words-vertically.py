import random


def generate(seed: int = 0) -> list[str]:
    """Generate uppercase words separated by exactly one space."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        words = [
            "".join(
                rng.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                for _ in range(1 + rng.randrange(10))
            )
            for _ in range(1 + i % 12)
        ]
        s = " ".join(words)
        call = f"candidate(s={s!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
