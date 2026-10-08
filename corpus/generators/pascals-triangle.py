DOMAIN_SIZE = 30


def generate(seed: int = 0) -> list[str]:
    """Enumerate every legal numRows value from 1 through 30."""
    return [f"candidate(numRows={count})" for count in range(1, 31)]
