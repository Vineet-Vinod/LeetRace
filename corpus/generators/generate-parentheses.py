DOMAIN_SIZE = 8


def generate(seed: int = 0) -> list[str]:
    # The entire legal input domain consists of n=1 through n=8.
    return [f"candidate(n={n})" for n in range(1, 9)]
