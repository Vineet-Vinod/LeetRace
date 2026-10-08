import random


def generate(seed: int = 0) -> list[str]:
    random.Random(seed)
    return [f"candidate(n={n})" for n in range(9)]


DOMAIN_SIZE = 9
