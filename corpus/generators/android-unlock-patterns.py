DOMAIN_SIZE = 81


def generate(seed: int = 0) -> list[str]:
    # The complete scalar input domain is every ordered pair in [1, 9] x [1, 9].
    return [f"candidate(m={m}, n={n})" for m in range(1, 10) for n in range(1, 10)]
