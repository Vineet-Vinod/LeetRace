DOMAIN_SIZE = 14


def generate(seed: int = 0) -> list[str]:
    # The complete legal input domain consists of n=1 through n=14.
    return [f"candidate(n={n})" for n in range(1, 15)]
