DOMAIN_SIZE = 11


def generate(seed: int = 0) -> list[str]:
    """The complete legal domain is the eleven LED counts from 0 through 10."""
    # The complete legal input domain has exactly eleven values.
    return [f"candidate(turnedOn={n})" for n in range(11)]
