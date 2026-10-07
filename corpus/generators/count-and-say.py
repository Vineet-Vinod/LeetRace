DOMAIN_SIZE = 30


def generate(seed: int = 0) -> list[str]:
    import random

    random.Random(seed)
    # The entire input domain has only 30 values; enumerate it exactly.
    return [f"candidate(n={n})" for n in range(1, 31)]
