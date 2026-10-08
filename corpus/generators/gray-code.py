DOMAIN_SIZE = 16


def generate(seed: int = 0) -> list[str]:
    # n is the entire legal input domain, 1 through 16.
    return [f"candidate(n={n})" for n in range(1, 17)]
