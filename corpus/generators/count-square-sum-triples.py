DOMAIN_SIZE = 250


def generate(seed: int = 0) -> list[str]:
    """The generator enumerates every legal n value from 1 through 250."""
    vals = list(range(1, 251))
    return [f"candidate(n={n})" for n in vals]
