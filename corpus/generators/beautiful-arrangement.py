def generate(seed: int = 0) -> list[str]:
    # The legal input domain is exactly the 15 integers from 1 through 15.
    return [f"candidate(n={n})" for n in range(1, 16)]


DOMAIN_SIZE = 15
