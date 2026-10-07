DOMAIN_SIZE = 9


def generate(seed: int = 0) -> list[str]:
    # The single integer parameter has exactly nine legal values.
    return [f"candidate(n={n})" for n in range(1, 10)]
