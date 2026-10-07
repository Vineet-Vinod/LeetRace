def generate(seed: int = 0) -> list[str]:
    # The full legal input domain is the 200 possible n values.
    return [f"candidate(n={n})" for n in range(1, 201)]


DOMAIN_SIZE = 200
