DOMAIN_SIZE = 100


def generate(seed: int = 0) -> list[str]:
    """Enumerate every legal x in the stated finite domain 1 through 100."""
    return [f"candidate(x={x})" for x in range(1, 101)]
