DOMAIN_SIZE = 45


def generate(seed: int = 0) -> list[str]:
    """Enumerate every legal input because n is restricted to 1 through 45."""
    return [f"candidate(n={n})" for n in range(1, 46)]
