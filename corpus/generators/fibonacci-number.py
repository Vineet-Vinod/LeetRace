import random

DOMAIN_SIZE = 31


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: Exhaustive legal n domain [0,30]."""
    rng = random.Random(seed)
    values = list(range(31))
    rng.shuffle(values)
    return [f"candidate(n={value})" for value in values]
