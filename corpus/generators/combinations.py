DOMAIN_SIZE = 210


def generate(seed: int = 0) -> list[str]:
    return [f"candidate(n={n}, k={k})" for n in range(1, 21) for k in range(1, n + 1)]
