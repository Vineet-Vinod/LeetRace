import random


def generate(seed: int = 0) -> list[str]:
    """Generate lowercase source strings and nonempty lowercase dictionary words."""
    rng = random.Random(seed)
    calls = []
    seen = set()
    i = 0
    while len(calls) < 600:
        s = "".join(rng.choice("abcde") for _ in range(1 + i % 40))
        dictionary = [
            "".join(rng.choice("abcde") for _ in range(1 + rng.randrange(12)))
            for _ in range(1 + i % 15)
        ]
        call = f"candidate(s={s!r}, dictionary={dictionary!r})"
        i += 1
        if call not in seen:
            seen.add(call)
            calls.append(call)
    return calls
