DOMAIN_SIZE = 240


def generate(seed: int = 0) -> list[str]:
    # Eight legal bases times thirty legal counts gives the complete 240-input domain.
    return [f"candidate(k={k}, n={n})" for k in range(2, 10) for n in range(1, 31)]
