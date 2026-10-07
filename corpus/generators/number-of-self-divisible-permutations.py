def generate(seed: int = 0) -> list[str]:
    return [f"candidate(n={n})" for n in range(1, 13)]


DOMAIN_SIZE = 12
