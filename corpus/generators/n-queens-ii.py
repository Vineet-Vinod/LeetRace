DOMAIN_SIZE = 9


def generate(seed: int = 0) -> list[str]:
    # The sole argument is an integer in [1,9], so these are the entire domain.
    return [f"candidate(n={n})" for n in range(1, 10)]
