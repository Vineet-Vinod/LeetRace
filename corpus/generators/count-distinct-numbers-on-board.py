import random

DOMAIN_SIZE = 100


def generate(seed: int = 0) -> list[str]:
    random.Random(seed)  # The legal domain is fully enumerated.
    return [f"candidate(n={n})" for n in range(1, 101)]
