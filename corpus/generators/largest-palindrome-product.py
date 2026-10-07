DOMAIN_SIZE = 8


def generate(seed: int = 0) -> list[str]:
    # The entire legal domain consists of the eight integers 1 through 8.
    return [f"candidate(n={n})" for n in range(1, 9)]
