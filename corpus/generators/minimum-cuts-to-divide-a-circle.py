import random

DOMAIN_SIZE = 100


def generate(seed: int = 0) -> list[str]:
    """Generate distinct valid cases: n in [1,100]."""
    rng = random.Random(seed)
    values = list(range(1, 101))
    rng.shuffle(values)
    return [f"candidate(n={value})" for value in values]
