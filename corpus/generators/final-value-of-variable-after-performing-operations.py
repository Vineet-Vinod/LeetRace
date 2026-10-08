import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    calls: set[str] = set()
    choices = ["++X", "X++", "--X", "X--"]
    while len(calls) < 600:
        operations = [rng.choice(choices) for _ in range(rng.randint(1, 100))]
        calls.add(f"candidate(operations={operations!r})")
    return sorted(calls)
