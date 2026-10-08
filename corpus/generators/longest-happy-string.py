import random


def generate(seed: int = 0) -> list[str]:
    rng = random.Random(seed)
    values = set()
    while len(values) < 600:
        triple = (rng.randint(0, 100), rng.randint(0, 100), rng.randint(0, 100))
        if sum(triple) > 0:
            values.add(triple)
    return [f"candidate(a={a}, b={b}, c={c})" for a, b, c in sorted(values)]
