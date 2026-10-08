def generate(seed: int = 0) -> list[str]:
    # The full legal input domain has only 50 values, so enumerate it.
    return [f"candidate(n={n})" for n in range(1, 51)]


DOMAIN_SIZE = 50
