def generate(seed: int = 0) -> list[str]:
    return [f"candidate(n={n})" for n in range(2, 1001, 2)]


DOMAIN_SIZE = 500
