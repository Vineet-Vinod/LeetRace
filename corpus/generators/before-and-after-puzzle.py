import random


def generate(seed: int = 0) -> list[str]:
    """Generate 600 unique lists of valid lowercase phrases (no empty or repeated spaces)."""
    rng = random.Random(seed)
    vocab = [
        "amber",
        "birch",
        "cobalt",
        "dune",
        "ember",
        "frost",
        "grove",
        "harbor",
        "indigo",
        "jade",
        "kindle",
        "linen",
    ]
    calls: list[str] = []
    seen: set[str] = set()
    i = 0
    while len(calls) < 600:
        n = 1 + i % 12
        phrases = [
            " ".join(rng.choice(vocab) for _ in range(1 + rng.randrange(4)))
            for _ in range(n)
        ]
        assert 1 <= n <= 100 and all(
            1 <= len(p) <= 100 and "  " not in p for p in phrases
        )
        call = f"candidate(phrases={phrases!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
