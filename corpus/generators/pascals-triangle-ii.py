DOMAIN_SIZE = 34


def generate(seed: int = 0) -> list[str]:
    return [f"candidate(rowIndex={value})" for value in range(34)]
